from django.shortcuts import render,redirect
from .models import Blogs

# Create your views here.


def newBlog(request):
    if request.method=="POST":
        blog_title=request.POST.get("blog_title")
        blog_content=request.POST.get("blog_content")
        blogs=Blogs.objects.create(content=blog_content,title=blog_title)
        blogs.save()
        return redirect('home')

    return render(request,'newBlog.html')