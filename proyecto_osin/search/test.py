import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

print("Ingresa el parametro correcto")
nombre = input()
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
driverPath = "driver/chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath, chrome_options=option)
browser.get("https://twitter.com/search?f=users&q={}&src=typd".format(nombre))
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
soup = bs(source_data,"html.parser")
if(soup.findAll(['script', 'style'])):
    [x.extract() for x in soup.findAll(['script', 'style'])]
        
if(soup.findAll(['meta'])):
    [y.extract() for y in soup.findAll(['meta'])]
        
if(soup.findAll(['noscript'])):
    [z.extract() for z in soup.findAll(['noscript'])]  
        
if(soup.findAll(['link'])):
    [a.extract() for a in soup.findAll(['link'])]

response=[]
for item in soup.select('.GridTimeline > div > div > div > div > div > div'):
    result={}
    result['nombre']=item.select_one(".ProfileCard-userFields > div > div > a").text.strip()
    result['link_tw']= "https://twitter.com{}".format(item.select_one("div > span > a")['href'])
    response.append(result)

print(response)
print(len(response))
