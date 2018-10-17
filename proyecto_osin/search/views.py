from django.shortcuts import render, redirect
import requests
import time
from selenium import webdriver
import re, urllib.request as ur
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Auto
from .models import Facebook
from .models import Twitter
from .models import Github
from .models import Google
from .models import Instagram
from .models import PersonaRedes
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
from django.contrib.sessions.models import Session
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
        result['link']=item.select_one(" ._4bl7._3-90 > a")['href'] 
        result['img']= item.select_one(" ._4bl7._3-90 > a > img")['src']
        result['name']=item.select_one(" ._4bl7._3-90 > a > img")['alt'] 
        #result['name']=item.select_one("div > div > div.clearfix > div:nth-of-type(2) > div > a").text
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

@login_required(login_url="/accounts/login")
def creategoogle(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        img_google = valor['img_google']
        info_google = valor['info_google']
        nombre_google= valor['nombre_google']
        url_google=valor['url_google']
        mensaje={}
        try:
            google_exist=Google.objects.filter(url_google=url_google).exists()
            if(google_exist):
                mensaje['fail']="No se guardo, ya existe el registro"
            else:
                goog=Google.objects.create(img_google=img_google,info_google=info_google,nombre_google=nombre_google,url_google=url_google,estado=1)
                if(goog):
                    mensaje['success']="Se guardo exitosamente"
                else:
                    mensaje['fail']="No se guardo el registro"
             
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo el registro"

    return JsonResponse(mensaje)
    

@login_required(login_url="/accounts/login")
def creategit(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        biografia_github = valor['biografia_github']
        email_github = valor['email_github']
        img_github= valor['img_github']
        nick_github=valor['nick_github']
        nombre_github=valor['nombre_github']
        pagina_github=valor['pagina_github']
        pais_github=valor['pais_github']
        mensaje={}
        try:
            github_exist=Github.objects.filter(nick_github=nick_github).exists()
            if(github_exist):
                mensaje['fail']="No se guardo, ya existe el registro"
            else:
                git=Github.objects.create(biografia_github=biografia_github,email_github=email_github,img_github=img_github,nick_github=nick_github,nombre_github=nombre_github,pagina_github=pagina_github,pais_github=pais_github,estado=1)
                if(git):
                    mensaje['success']="Se guardo exitosamente"
                else:
                    mensaje['fail']="No se guardo el registro"
             
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo el registro"

    return JsonResponse(mensaje)
    
@login_required(login_url="/accounts/login")
def createasig(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        if(valor['idfb_id']==''):
            valor['idfb_id']=None
        
        if(valor['idtw_id']==''):
            valor['idtw_id']=None
        
        if(valor['idgoogle_id']==''):
            valor['idgoogle_id']=None
        
        if(valor['idgithub_id']==''):
            valor['idgithub_id']=None
        
        if(valor['idinstagram_id']==''):
            valor['idinstagram_id']=None
            
        idfb_id=valor['idfb_id']
        idpersona_id=valor['idpersona_id']
        idtw_id=valor['idtw_id']
        idgoogle_id=valor['idgoogle_id']
        idgithub_id=valor['idgithub_id']
        idinstagram_id=valor['idinstagram_id']
        idusuario_id = request.session["id_user"]
        estado=1
        mensaje={}
        try:
            cantidadRegistros=PersonaRedes.objects.filter(idfb_id=idfb_id,idpersona_id=idpersona_id,idtw_id=idtw_id,idgoogle_id=idgoogle_id,idgithub_id=idgithub_id,idinstagram_id=idinstagram_id,idusuario_id=idusuario_id).count()
            if(cantidadRegistros<1):
                perreds=PersonaRedes.objects.create(idfb_id=idfb_id,idpersona_id=idpersona_id,idtw_id=idtw_id,idgoogle_id=idgoogle_id,idgithub_id=idgithub_id,idinstagram_id=idinstagram_id,idusuario_id=idusuario_id,estado=1)
                if(perreds):
                    mensaje['success']="Se guardo exitosamente"
                else:
                    mensaje['fail']="No se guardo el registro" 
            else:
                mensaje['fail']="Ya se guardo anteriormente el registro."
 
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo el registro"

    return JsonResponse(mensaje)

@login_required(login_url="/accounts/login")
def createinstagram(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        nombre_instagram = valor['nombre_instagram']
        usuario_instagram = valor['usuario_instagram']
        url_instagram= valor['url_instagram']
        foto_instagram=valor['foto_instagram']
        seguidores_instagram=valor['seguidores_instagram']
        post_instagram=valor['post_instagram']
        siguiendo_instagram=valor['siguiendo_instagram']
        estado=1
        mensaje={}
        try:
            instagram_exist=Instagram.objects.filter(url_instagram=url_instagram).exists()
            if(instagram_exist):
                mensaje['fail']="No se guardo, ya existe el registro"
            else:
                instagram=Instagram.objects.create(nombre_instagram=nombre_instagram,usuario_instagram=usuario_instagram,url_instagram=url_instagram,foto_instagram=foto_instagram,seguidores_instagram=seguidores_instagram,post_instagram=post_instagram,siguiendo_instagram=siguiendo_instagram,estado=1)
                if(instagram):
                    mensaje['success']="Se guardo exitosamente"
                else:
                    mensaje['fail']="No se guardo el registro"
             
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo el registro"

    return JsonResponse(mensaje)
    


@login_required(login_url="/accounts/login")
def createtw(request):
    if(request.method == 'POST'):
        valor=json.loads(request.body.decode("utf-8"))
        inicio_tw = valor['inicio_tw']
        cant_tw = valor['cant_tw']
        url= valor['url']
        img_tw=valor['img_tw']
        nombre_tw=valor['nombre_tw']
        nombre_cuenta_tw=valor['nombre_cuenta_tw']
        pagina_web=valor['pagina_web']
        biografia=valor['biografia']
        seguidores=valor['seguidores']
        siguiendo=valor['siguiendo']
        tweets=valor['tweets']
        ubicacion=valor['ubicacion']
        likes=valor['likes']
        estado=1
        mensaje={}
        try:
            twitter_exist=Twitter.objects.filter(url=url).exists()
            if(twitter_exist):
                mensaje['fail']="No se guardo, ya existe el registro"
            else:
                twiiter=Twitter.objects.create(inicio_tw=inicio_tw,cant_tw=cant_tw,url=url,img_tw=img_tw,nombre_tw=nombre_tw,nombre_cuenta_tw=nombre_cuenta_tw,pagina_web=pagina_web,biografia=biografia,seguidores=seguidores,siguiendo=siguiendo,tweets=tweets,ubicacion=ubicacion,likes=likes,estado=1)
                if(twiiter):
                    mensaje['success']="Se guardo exitosamente"
                else:
                    mensaje['fail']="No se guardo el registro "
             
        except requests.exceptions.HTTPError as e:
            mensaje['fail']="No se guardo el registro"

    return JsonResponse(mensaje)
    

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
        response.append(i.text.strip())
    
    new_lista=list(filter(lambda x: ('http') in x, response))
    error_res="No existe página web"
    if(new_lista):
        str1 = ''.join(new_lista)
        return str1
    else:
        return error_res 
        


def getlinks(url):
    session = HTMLSession()
    soup = session.get(url)
    response=[]
    for a in soup.html.links:
        result={}
        if(a=="#"):
            response.append(a)
            response.remove("#")
        elif(a=="/"):
            response.append(a)
            response.remove("/")
        else:
            response.append(a)
    
    resp=sorted(list(set(response)))
    new_lista=list(filter(lambda x: ('#tabs' or '#tab') not in x, resp))
    valor=[]
    odd_num=list(filter(lambda x: 'http' not in x, new_lista))

    for itemr in odd_num:
        new_lista.remove(itemr)
        valor.append(url+itemr)
    
    for itemx in valor:
        new_lista.append(itemx)
    
    return new_lista 



@login_required(login_url="/accounts/login") 
def getcomercio(request):
    buscador=request.GET.get('buscador')
    url=request.GET.get('url')
    response=getcodersp(url)
    data=[]
    for urlitem in response:
        if(urlitem!='No hay data'):
            data.append(item_comercio(urlitem,buscador))
        else:
            data.append("No hay data")
    res={
    'info':data
    }
    return JsonResponse(res)
    


def getcodersp(url): 
    lista=getlinks(url)
    if(lista):
        response=[]
        for item in lista:
            rest={}
            try:
                result = requests.get(item)
                if(result.status_code != 404 ):
                    response.append(item)   
            except requests.exceptions.RequestException as e:
                response.append("UrlInvalida") 

        new_lista_x=list(filter(lambda x: 'UrlInvalida' not in x, response))
        return new_lista_x
    else:
        new_lista_x=[]
        new_lista_x.append('No hay data')
        return new_lista_x
    
         

    
def item_comercio(urlitem,buscador):
    resp = requests.get(urlitem,verify=False)
    txt = resp.text
    mayuscula_buscador=buscador.upper()
    minuscular_buscador=buscador.lower()
    capital_buscador=buscador.capitalize()
    getHtml=BeautifulSoup(txt,"html.parser")

    if(getHtml.findAll(['script', 'style'])):
        [x.extract() for x in getHtml.findAll(['script', 'style'])]
    
    if(getHtml.findAll(['meta'])):
        [y.extract() for y in getHtml.findAll(['meta'])]
        
    if(getHtml.findAll(['noscript'])):  
        [z.extract() for z in getHtml.findAll(['noscript'])]

    if(getHtml.findAll(['link'])):
        [a.extract() for a in getHtml.findAll(['link'])]
 
    variable=''
    if(getHtml.title):
        variable=getHtml.title.string
    else:
        variable="Pagina sin titulo"

    cadena=getHtml.text
    strip = strip_tags(cadena)

    minuscula=strip.count(minuscular_buscador)
    mayuscula=strip.count(mayuscula_buscador)
    capital=strip.count(capital_buscador)
    res=minuscula+mayuscula+capital
   
    data={
        'link':urlitem,
        'titulo' : variable,
        'coincidencias' : res
    }

    return data


@login_required(login_url="/accounts/login")
def getgoogle(request):
    buscador=request.GET.get('buscador')
    soup=get_doc("https://plus.google.com/s/{}/people".format(buscador))
    response=[]
    for item in soup.select(".H68wj.t1KkGe > .NzRmxf.vCjazd"):
        result={}
        result['img_google']=item.select_one("a > img")['src']
        result['url_google']="https://plus.google.com/{}".format(item.select_one("a")['href'].replace("./", ""))      
        result['nombre_google']=item.select_one("a > div > div").text
        if(item.select_one("a > div:nth-of-type(2) > span")):
            result['info_google']=item.select_one("a > div:nth-of-type(2) > span").text
        else:
            result['info_google']="No hay info"
        response.append(result) 
  
    data={'info_all':response}
    return JsonResponse(data) 

@login_required(login_url="/accounts/login") 
def gethit(request):
    buscador=request.GET.get('buscador')
    pagina=request.GET.get('pagina')
    if(pagina!=''):
        soup=get_doc("https://github.com/search?p={}&q={}&type=Users".format(pagina,buscador))
    else:
        soup=get_doc("https://github.com/search?p={}&q={}&type=Users".format(1,buscador))
        
    response=[]

    for item in soup.select(".col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > #user_search_results > div > .user-list-item.f5.py-4"):
        result={}
        result['img_github']=item.select_one("div > a > img")['src']
        result['nick_github']="https://github.com/{}".format(item.select_one("div > div > a").text)   
        result['nombre_github']=item.select_one("div > div > div").text
        result['email_github']=gethits(item.select_one("div > div > a").text)
        result['pagina_github']=getgit(item.select_one("div > div > a").text)
        if(item.select_one("div > div > p")):
            result['biografia_github']=item.select_one("div > div > p").text.strip()
        else:
            result['biografia_github']="No existe biografia"
        
        for i in item.select("div > div > ul > li"):
            result['pais_github']=i.text.strip()
        
        response.append(result) 
  
    data={'info_all':response}
    return JsonResponse(data) 

@login_required(login_url="/accounts/login") 
def getinstadet(request):      
    username_instahram=request.GET.get('username_instahram')
    soup=get_doc("https://web.stagram.com/{}".format(username_instahram))
    response=[]
    for i in soup.select(".userdata.clearfix.text-center.mb-4 > p"):
        for x in i.select("span"):
            result={}
            response.append(x.text.strip())
    
    for i in soup.select(".userdata.clearfix.text-center.mb-4 > p"):
        response.append(i.text.strip())
    
    #data={'post':response[0],'seguidores':response[1],'siguiendo':response[2]}
    data={'info':response}
    return JsonResponse(data)

@login_required(login_url="/accounts/login") 
def getinsta(request):
    buscador=request.GET.get('buscador')
    soup=get_doc("https://web.stagram.com/search?query={}".format(buscador))
    response=[]
    response_inta=[]
    for i in soup.select(".row.photolist > .col-6.col-xs-12.col-sm-6.col-md-4.col-lg-3.mb-4"):
        result_inta={}
        result_inta['logo_inta']=i.select_one("div > a > img")['src']
        result_inta['user_inta']=i.select_one("div > a > div > h4").text
        result_inta['name_inta']=i.select_one("div > a > div > p").text
        result_inta['nick_inta']="https://www.instagram.com/{}/".format(i.select_one("div > a > div > h4").text)
        #result_inta['detalles_inta']=getinstadet(result_inta['user_inta'])
        response_inta.append(result_inta) 

         
    for item in soup.select(".row.photolist > .col-6.col-sm-4.col-md-3.mb-4"):
        result={}
        result['logo_inta']="https://web.stagram.com{}".format(item.select_one("div > a > img")['src'])   
        result['nick_inta']=item.select_one("div > a > div > h4").text
        result['name_inta']=item.select_one("div > a > div > span").text
        response.append(result) 

    data={'info_post':response,'info_users':response_inta}
    return JsonResponse(data) 


def gettrending(request):
    buscador=request.GET.get('buscador')
    soup = get_doc('https://trends24.in/{}'.format(buscador))
    tems=soup.select('div#trend-list')
    response=[]
    for i in tems:
        div1=i.select_one('div > ol')
        lista=div1.select('li')
        for it in lista:
            listali=it.select_one('a').text
            response.append(listali)

    data={'info_trending':response}
    return JsonResponse(data) 
     

@login_required(login_url="/accounts/login") 
def gettw(request):
    buscador=request.GET.get('buscador')
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    driverPath = r"C:/driver/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driverPath, chrome_options=option)
    browser.get("https://twitter.com/search?f=users&vertical=default&q={}&src=typd".format(buscador))
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    source_data = browser.page_source
    browser.close() 
    soup = BeautifulSoup(source_data,"html.parser")
    if(soup.findAll(['script', 'style'])):
        [x.extract() for x in soup.findAll(['script', 'style'])]
        
    if(soup.findAll(['meta'])):
        [y.extract() for y in soup.findAll(['meta'])]
        
    if(soup.findAll(['noscript'])):
        [z.extract() for z in soup.findAll(['noscript'])]  
        
    if(soup.findAll(['link'])):
        [a.extract() for a in soup.findAll(['link'])]
    # soup=get_doc("https://twitter.com/search?f=users&vertical=default&q={}&src=typd".format(buscador))
    response=[]
    for item in soup.select('.GridTimeline > div > div > div > div > div > div'):
        result={}
        result['nombre']=item.select_one(".ProfileCard-userFields > div > div > a").text
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
            result['pagina']=infot.select_one(".ProfileHeaderCard-url > span:nth-of-type(2) > a").text
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
    for item in infotws.select('div#timeline > div > div:nth-of-type(2) > ol > li > div > div:nth-of-type(2)'):
        result={}
        result['cabezera_fecha']= item.select_one("div > small > a")['title']
        if(item.select_one(".js-tweet-text-container > p")):
            result['texto_tweet']=item.select_one(".js-tweet-text-container > p").text   
        else:
            result['texto_tweet']=""
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
    
    

    