from django.urls import path
from . import views


urlpatterns = [
    path('',views.newBlog,name='new_blog'),
   
]
