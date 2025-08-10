from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bs4 import BeautifulSoup
import requests
# Create your views here.


def register_user(request):
    return render(request,'register.html')


def new_user(request):
    if (request.method=='POST'):
        firstname=request.POST.get('firstname')
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
       # print(f"Received: {firstname}, {lastname}, {email}, {password}")
        username=firstname+lastname
        c=User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect('user_login')
    return render(request,"register.html")

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
       # print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"invalid credentials"})
    
    return render(request,'login.html')

######################################################################################################
#*************************  for all bikes  **********************************************************
########################################################################################################

def home(request):
    all_bURL="https://www.bikewale.com/"
    response1=requests.get(all_bURL)
    #print(response1)
    home_soup=BeautifulSoup(response1.content,"html.parser")
    all_bike_images=[]
    all_bike_names=[]
    all_bike_links=[]
    allbike_names=home_soup.find_all("div",class_="o-jr o-j1 o-jK o-ei")
    for i in allbike_names:
        bikenames=i.get_text()
        all_bike_names.append(bikenames)

    allbike_images=home_soup.find_all("div", class_=lambda c:c and "PfHybH" in c )
    for i in allbike_images:
         img_tag=i.find("img")
         bikeimages= img_tag.get("data-src") or img_tag["src"]
         all_bike_images.append(bikeimages)

    allbike_links=home_soup.find_all("a", class_=lambda c: c and "o-d" in c and "o-os" in c)
    for i in allbike_links:
        a_tag=i.get("href")
        final_link=all_bURL + a_tag
        all_bike_links.append(final_link)

    all_bikes=zip(all_bike_names,all_bike_images,all_bike_links)  

    return render(request,"home.html",{"all_bike_details":all_bikes})





######################################################################################################
#*************************  for bajaj bikes  **********************************************************
######################################################################################################

def bike(request):
   url='https://www.bikewale.com/bajaj-bikes/'
   response=requests.get(url)
   #print(response)
   soup=BeautifulSoup(response.content,'html.parser')
   #print(soup)
   b_title=soup.find_all("h3",class_="o-j4 o-jq o-hM o-c4")
   bajlink=[]
   prices=[]
   title=[]    
   images=[]

#    for i in b_title:
#        biketitle=i.get_text()
#        title.append(biketitle)
    
   b_link=soup.find_all("a",class_="o-f o-aF o-jJ o-eQ")
   
   for i in b_link:
       bikelink=i.get("href")
       biketitle=i.find("h3").get_text()
       title.append(biketitle)
       bajaj_url='https://www.bikewale.com/'
       link=bajaj_url+bikelink
       bajlink.append(link)

   b_img = soup.find_all("div", class_=lambda c:c and "PhYMAu" in c)
   for i in b_img:
       img_tag=i.find("img")
       bikeimage= img_tag.get("data-src") or img_tag["src"]
       images.append(bikeimage)

   b_price = soup.find_all("span", class_="o-jJ o-jr o-j3 o-kJ")
   for i in b_price:
       bikeprice=i.get_text()
       prices.append(bikeprice)
       

   bajabike=zip(title,bajlink,images,prices)

   return render(request,'bajaj.html',{"b_bikes":bajabike})
    


