from django.shortcuts import render, redirect
import requests
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Auto
from .forms import AutoForm
from fullcontact import FullContact
import urllib.request
import clearbit
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
    return urllib.request.urlopen(req,data).read()

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
   
def gettw(request):
    soup=get_doc("https://twitter.com/search?f=users&vertical=default&q=omarmontoya&src=typd")
    return HttpResponse("dfdf") 

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
    
    

    