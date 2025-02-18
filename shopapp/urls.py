
from django.contrib import admin
from django.urls import path
from shopapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('gallary/', views.images),
]
