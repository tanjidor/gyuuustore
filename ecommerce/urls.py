from django.urls import path 
from . import views 

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('kontak/', views.kontak, name='kontak'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]