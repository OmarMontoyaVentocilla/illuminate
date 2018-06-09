from django.shortcuts import render, redirect
import requests
import re, urllib.request as ur
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Auto
from .forms import AutoForm
from fullcontact import FullContact
import urllib.request
import clearbit
import json
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
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
    google=requests.get(url)
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
    for item in soup.select(".fbProfileEditExperiences li div div div.clearfix div:nth-of-type(2) div span"):
        places.append(item.text)
    for item in soup.select(".fbProfileEditExperiences li div div div.clearfix div:nth-of-type(2) div div.fsm"):
        places_c.append(item.text)
    for index, place in enumerate(places):
        response.append({places_c[index] : place})
    return response

def get_studies(soup):
    response = []
    study = []
    work = []
    for item in soup.select("#pagelet_eduwork > div > div"):
        academic_title = item.select_one("span[role=heading]").text
        if(academic_title == "Empleo"):
            for l in item.select("ul.fbProfileEditExperiences li.fbEditProfileViewExperience div div.clearfix div div a"):
                work.append({"empleo" : l.text})
        elif(academic_title == "Formación académica"): 
            for l in item.select("ul.fbProfileEditExperiences li.fbEditProfileViewExperience div div.clearfix div div a"):
                study.append({"formacion_academica" : l.text})
    
    response.append(work)
    response.append(study)
    return response

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
    

def gethit(request):
    soup=get_doc("https://github.com/search?q=omar&type=Users")
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



@login_required(login_url="/accounts/login") 
def gettw(request):
    soup=get_doc("https://twitter.com/search?f=users&vertical=default&q=omar%20mv&src=typd")
    response=[]
    for item in soup.select('.GridTimeline > div > div > div > div > div > div'):
        result={}
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
            result['ubicacion']="ninguna"
        
        if(infot.select_one(".ProfileHeaderCard-url > span:nth-of-type(2) > a")):
            result['pagina']=infot.select_one(".ProfileHeaderCard-url > span:nth-of-type(2) > a")['title']
        else:
            result['pagina']="ninguna"
        
        if(infot.select_one(".ProfileHeaderCard-joinDate > span:nth-of-type(2)")):
            result['inicio_tw']=infot.select_one(".ProfileHeaderCard-joinDate > span:nth-of-type(2)").text
        else:
            result['inicio_tw']="ninguna"
        
        result['img_tw']= item.select_one("a > img")['src']
        result['nombre_tw']= "@{}".format(item.select_one("div > span > a > span > b").text)
        result['biografia'] = item.select_one("div > p").text
        result['info']={
                        'tweets':gettwts(result['link_tw'])
                       }
    
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
    #data={'info_all':response}
    return response

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
    
    

    