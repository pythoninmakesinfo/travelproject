
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from  . import views
from startinmake import settings

urlpatterns = [

   path('',views.demo,name='index.html'),

]
