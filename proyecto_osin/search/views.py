from django.shortcuts import render, redirect
import requests
import re, urllib.request as ur
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Auto
from .models import Facebook
from .forms import AutoForm
from fullcontact import FullContact
import urllib.request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import clearbit
import json
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from requests_html import HTMLSession
# # Create your views here.
def create_auto(request):
    form=AutoForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect('list_auto')
    
    return render(request,'auto-forms.html',{'form':form})

def get_clearbit(email):
    clearbit.key = 'sk_5d3ef2a9dc8abf26a176c2846558b8a4'
    return clearbit.Enrichment.find(email=email, stream=True)

def get_fullcontact(email):
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer ZghAT1ObykblNeCSRLgKl420jAMxJDXZ')
    data = json.dumps({
      "email": email
    }).encode("utf-8")
    response = urllib.request.urlopen(req,data)
    data={
        "response":response
    }
    return JsonResponse(data)

def get_doc(url):
    google=requests.get(url, verify=False)
    soup=BeautifulSoup(google.content,"html.parser")
    to_extract=soup.findAll("script")
    for item in to_extract:
        item.extract()
    to_extract=soup.findAll("style")
    for item in to_extract:
        item.extract()
    result=BeautifulSoup(str(soup).replace("<!--",""),"html.parser") 
    return result

def get_name(soup):
    return soup.find('meta',property='og:title')['content']

def get_bio(soup):
    if(soup.select_one("#pagelet_bio div ul")):
        return soup.select_one("#pagelet_bio div ul").text
    else:
        return ''

def get_photo(soup):
    id=get_fb_id(soup)
    return "https://graph.facebook.com/{}/picture?type=large".format(id)

def get_fb_id(soup):
    return soup.find('meta', property='al:android:url')['content'].replace('fb://profile/','')

def get_places(soup):
    response=[]
    places_c=[]
    places=[]
    for item in soup.select("ul.uiList.fbProfileEditExperiences._4kg._4ks #current_city"):
        result={}
        result['ciudad_actual']=item.select_one("div > div > div > div > div > div:nth-of-type(2) > span > a").text
        places.append(result)
    return places

def get_studies(soup):
    study = []
    for item in soup.select("#pagelet_eduwork > div > div"):
        academic_title = item.select_one("span[role=heading]").text  
        if(academic_title == "Formación académica"): 
            for l in item.select("ul.fbProfileEditExperiences li.fbEditProfileViewExperience div div.clearfix div div a"):
                study.append({"formacion_academica":l.text})

    return study

def get_work(soup):
    work = []
    for item in soup.select("#pagelet_eduwork > div > div"):
        academic_title = item.select_one("span[role=heading]").text
        if(academic_title == "Empleo"):
            for l in item.select("ul.fbProfileEditExperiences li.fbEditProfileViewExperience div div.clearfix div div a"):
                work.append({"empleo":l.text})

    return work

def search_by_name(url,pag):
    soup=get_doc("https://www.facebook.com/public/{}?page={}".format(url,pag))
    response=[]
    for item in soup.select('div#BrowseResultsContainer > div > div > div > div '):
        result={}
        result['link']=item.select_one("a")['href'] 
        result['img']= item.select_one("a > img")['src']
        result['name']=item.select_one("div > div > div.clearfix > div:nth-of-type(2) > div > a").text
        response.append(result)
    
    return response


@login_required(login_url="/accounts/login") 
def createfacebook(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        idfb = valor['idfb']
        name = valor['name']
        biografia= valor['biografia']
        foto=valor['foto']
        url=valor['url']
        cstudies=valor['cstudies']
        clugares=valor['clugares']
        ctrabajo=valor['ctrabajo']
        estado=1
        mensaje={}
        try:
            facebook=Facebook.objects.create(idfb=idfb,nombres=name,biografia=biografia,foto=foto,url=url,trabajo=ctrabajo,lugar=clugares,estudio=cstudies,estado=estado)
            if(facebook):
                mensaje['success']="Se guardo exitosamente"
            else:
                mensaje['fail']="No se guardo ya existe el registro"
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo ya existe el registro"

    return JsonResponse(mensaje)

def getlistfacebook(request):
    fb=Facebook.objects.filter(estado=1)
    data=json.dumps({"fb":fb})
    return data


@login_required(login_url="/accounts/login") 
def get_details(request):
    url=request.GET.get('url')
    doc = get_doc(url)
    response = {}
    response['name'] = get_name(doc)
    response['id'] = get_fb_id(doc)
    response['photo'] = get_photo(doc)
    response['bio'] = get_bio(doc)
    response['places'] = get_places(doc)
    response['studies'] = get_studies(doc)
    response['work'] = get_work(doc)
    response['url'] = url
    data={
        'info_all':response
    }
    return JsonResponse(data)

def gethits(username):
    f = ur.urlopen("https://api.github.com/users/{}/events/public".format(username))
    s = f.read().decode('utf-8')
    number=re.findall(r"\+\d{2}\s?0?\d{10}",s)
    email=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
    if(len(email)>0):
        data=email[0]
    else:
        data="No existe email"  
    return data


def getgit(url_nick):
    soup=get_doc("https://github.com/{}".format(url_nick))
    response=[]
    for i in soup.select("ul.vcard-details.border-top.border-gray-light.py-3 > li"):
        result={}
        result['web']=i.text.strip()     
        response.append(result)
    
    error_res="No existe página web"
    if(4==len(response)):
        data=response[3]
    elif(3==len(response)):
        data=error_res
    elif(2==len(response)):
        data=error_res
    elif(1==len(response)):
        data=error_res   
    else:
        data=error_res
    return data 




         

def getgoogle(request):
    soup=get_doc("https://plus.google.com/s/omar%20montoya/people")
    response=[]
    for item in soup.select(".H68wj.t1KkGe > .NzRmxf.vCjazd"):
        result={}
        result['img_google']=item.select_one("a > img")['src']
        result['id_google']=item.select_one("a")['href'].replace("./", "")
        result['nombre_google']=item.select_one("a > div > div").text
        if(item.select_one("a > div:nth-of-type(2) > span")):
            result['info_google']=item.select_one("a > div:nth-of-type(2) > span").text
        else:
            result['info_google']="No hay info"
        response.append(result) 
  
    data={'info_all':response}
    return JsonResponse(data) 

# def getlinken(request):
    # soup=get_doc("https://pe.linkedin.com/pub/dir/Omar/Montoya")
    # response=[]
    # result={}
    # if(soup.select(".primary-section > .professionals.section.blue-cta-enabled > ul.content > li.has-country-specific-link")):
    #      result['x']="bien"
    # else:
    #     result['x']="mal"
    # response.append(result)
    # data={'info_all':response}
    # return JsonResponse(data) 
    # return ''
        
    # for item in soup.select(".primary-section > .professionals.section.blue-cta-enabled > ul.content > li"):
    #     result={}
    #     result['fff']="fdfdf"
    #     # result['link_linkend']=item.select_one("div > a")['href']
    #     # result['foto_linkend']=item.select_one("a > img")['src']
    #     # result['user_linkend']=item.select_one("div > h3 > a").text
    #     # result['info_trabactu_linkend']=item.select_one("div > p").text
    #     # result['info_lugar_linkend']=item.select_one("div > dl").text
    #     response.append(result)

    # data={'info_all':response}
    # return JsonResponse(data) 


    

@login_required(login_url="/accounts/login") 
def gethit(request):
    buscador=request.GET.get('buscador')
    soup=get_doc("https://github.com/search?q={}&type=Users".format(buscador))
    response=[]

    for item in soup.select(".column.three-fourths.codesearch-results > div > #user_search_results > div > .user-list-item.f5.py-4"):
        result={}
        result['img_github']=item.select_one("div:nth-of-type(2) > a > img")['src']
        result['nick_github']="https://github.com/{}".format(item.select_one("div:nth-of-type(2) > div > a").text)   
        result['nombre_github']=item.select_one("div:nth-of-type(2) > div > span").text
        result['email_github']=gethits(item.select_one("div:nth-of-type(2) > div > a").text)
        result['pagina_github']=getgit(item.select_one("div:nth-of-type(2) > div > a").text)
        if(item.select_one("div:nth-of-type(2) > div > p")):
            result['biografia_github']=item.select_one("div:nth-of-type(2) > div > p").text.strip()
        else:
            result['biografia_github']="No existe biografia"
        
        for i in item.select("div:nth-of-type(2) > div > ul > li"):
            result['pais_github']=i.text.strip()
            response.append(result) 
  
    data={'info_all':response}
    return JsonResponse(data) 


def getinstadet(url):
    soup=get_doc("https://web.stagram.com/{}".format(url))
    response=[]
    for i in soup.select(".userdata.clearfix.text-center.mb-4 > p"):
        for x in i.select("span"):
            result={}
            result['resultado']=x.text
            response.append(result)
    
    data={'post':response[0],'seguidores':response[1],'siguiendo':response[2]}
    #data={'post':response[0]}
    return response

@login_required(login_url="/accounts/login") 
def getinsta(request):
    buscador=request.GET.get('buscador')
    soup=get_doc("https://web.stagram.com/search?query={}".format(buscador))
    response=[]
    response_inta=[]
    for i in soup.select(".row.photolist > .col-6.col-xs-12.col-sm-6.col-md-4.col-lg-3.mb-4"):
        result_inta={}
        result_inta['logo_inta']=i.select_one("div > a > img")['src'] 
        result_inta['nick_inta']="https://www.instagram.com/{}/".format(i.select_one("div > a > div > h4").text)
        result_inta['name_inta']=i.select_one("div > a > div > p").text
        #result_inta['detalles'] = getinstadet(i.select_one("div > a > div > h4").text)
        response_inta.append(result_inta)
    
    for item in soup.select(".row.photolist > .col-6.col-sm-4.col-md-3.mb-4"):
        result={}
        result['logo_inta']="https://web.stagram.com{}".format(item.select_one("div > a > img")['src'])   
        result['nick_inta']=item.select_one("div > a > div > h4").text
        result['name_inta']=item.select_one("div > a > div > span").text
        response.append(result) 

    data={'info_post':response,'info_users':response_inta}
    return JsonResponse(data) 
    


 

@login_required(login_url="/accounts/login") 
def gettw(request):
    buscador=request.GET.get('buscador')
    soup=get_doc("https://twitter.com/search?f=users&vertical=default&q={}&src=typd".format(buscador))
    response=[]
    iterador=0
    for item in soup.select('.GridTimeline > div > div > div > div > div > div'):
        result={}
        result['id']= iterador+1
        result['link_tw']= "https://twitter.com{}".format(item.select_one("div > span > a")['href'])
        infot=get_doc(result['link_tw'])

        if(infot.select_one(".ProfileCanopy-nav > div > ul > li > a > span:nth-of-type(3)")):
            result['tweets']=infot.select_one(".ProfileCanopy-nav > div > ul > li > a > span:nth-of-type(3)").text.strip()
        else:
            result['tweets']="0 tweets"
        
        if(infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(2) > a > span:nth-of-type(3)")):
            result['siguiendo']=infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(2) > a > span:nth-of-type(3)").text.strip() 
        else:
            result['siguiendo']="0 following"

        if(infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(3) > a > span:nth-of-type(3)")):
            result['seguidores']=infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(3) > a > span:nth-of-type(3)").text.strip() 
        else:
            result['seguidores']="0 followers"
        
        if(infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(4) > a > span:nth-of-type(3)")):
            result['likes']=infot.select_one(".ProfileCanopy-nav > div > ul > li:nth-of-type(4) > a > span:nth-of-type(3)").text.strip() 
        else:
            result['likes']="0 likes"
        
        if(infot.select_one(".ProfileHeaderCard-location > span:nth-of-type(2) > a")):
            result['ubicacion']=infot.select_one(".ProfileHeaderCard-location > span:nth-of-type(2) > a").text 
        else:
            result['ubicacion']="Ninguna"
        
        if(infot.select_one(".ProfileHeaderCard-url > span:nth-of-type(2) > a")):
            result['pagina']=infot.select_one(".ProfileHeaderCard-url > span:nth-of-type(2) > a")['title']
        else:
            result['pagina']="Ninguna"
        
        if(infot.select_one(".ProfileHeaderCard-joinDate > span:nth-of-type(2)")):
            result['inicio_tw']=infot.select_one(".ProfileHeaderCard-joinDate > span:nth-of-type(2)").text
        else:
            result['inicio_tw']="Ninguna"
        
        result['img_tw']= item.select_one("a > img")['src']
        result['nombre_tw']= "@{}".format(item.select_one("div > span > a > span > b").text)
        
        if(item.select_one("div > p")):
            if(item.select_one("div > p").text!=''):
                result['biografia'] = item.select_one("div > p").text
            else:
                result['biografia'] = "Ninguna"         
        else:
            result['biografia']="Ninguna"
            
        result['info']=gettwts(result['link_tw'])

        response.append(result)
      
    data={'info_all':response}
    return JsonResponse(data) 


def gettwts(url):
    infotws=get_doc(url)
    response=[]
    for item in infotws.select('.ProfileTimeline > div > div:nth-of-type(2) > ol > li > div > div:nth-of-type(2)'):
        result={}
        result['cabezera_fecha']= item.select_one("div > small > a")['title']
        if(item.select_one(".js-tweet-text-container > p")):
            result['texto_tweet']=item.select_one(".js-tweet-text-container > p").text   
        else:
            result['texto_tweet']="no hay dato"
        response.append(result)
    return len(response)

@login_required(login_url="/accounts/login")
def getAuto(request):
    buscador=request.GET.get('buscador')
    pag=request.GET.get('pag')
    if(pag==''):
        valor=search_by_name(buscador,1)
    elif(pag!=''):
        valor=search_by_name(buscador,pag)  

    data={
        'valor':valor
    }
    return JsonResponse(data)

@login_required(login_url="/accounts/login")        
def customSearch(request):
    return render(request,'custom.html')    
      
@login_required(login_url="/accounts/login")
def list_auto(request):
    autos=Auto.objects.all()
    return render(request,'auto.html',{'autos':autos})

def update_auto(request,id):
    auto=Auto.objects.get(id=id)
    form=AutoForm(request.POST or None, instance=auto)
    if(form.is_valid()):
        form.save()
        return redirect('list_auto')
    
    return render(request,'auto-forms.html',{'form':form, 'auto':auto})

def delete_auto(request,id):
    auto=Auto.objects.get(id=id)

    if(request.method=='POST'):
        auto.delete()
        return redirect('list_auto')
    
    return render(request,'auto-delete-confirm.html',{'auto':auto})
    
    

    