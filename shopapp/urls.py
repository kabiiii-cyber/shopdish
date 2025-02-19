
from django.contrib import admin
from django.urls import path
from setuptools.extern import names

from shopapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('gallary/', views.images,name="gallary"),
    path('', views.about,name="about"),
]
