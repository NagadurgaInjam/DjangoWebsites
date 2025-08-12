from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from newblog.models import Blogs



def userlogin_d(request):
   # return render(request,"home.html")
    return home(request)

def userlogin(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        users=authenticate(username=username,password=password)
        if users is not None:
            login(request,users)
            return home(request)
           # return render(request,"home.html")
        else:
            return render(request,"login.html",{'Error':'invalid login'})
    return render(request,"login.html")

def user_register(request):

    if request.method=="POST":
        username=request.POST.get("userfullname")
        mail=request.POST.get("email")
        password=request.POST.get("userpassword")
        users=User.objects.create_user(username=username,email=mail,password=password)
        return render(request,'login.html')
    else:
        return render(request,'register.html',{'error':"Invalid user"})
        
    
def home(request):
    blogs=Blogs.objects.all()
    
    print(blogs)
    return render(request,'home.html',{'blogs':blogs})


def edit_blog(request,pk):
    editblog=get_object_or_404(Blogs,pk=pk)
    
    if request.method =="POST":
        new_blog=request.POST['newblog']
        editblog.content=new_blog
        editblog.save()
        return redirect("home")
    else:
        return render(request,'editblog.html',{'editblog':editblog})

    
def delete_blog(request,pk):
    deleteblog=get_object_or_404(Blogs,pk=pk)
    deleteblog.delete()
    
    return redirect("home")