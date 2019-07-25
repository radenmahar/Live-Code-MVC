from django.urls import path
from . import views

urlpatterns = [
    path('', views.HalamanHome, name = 'home'),
    path('base/', views.Halamanbase, name = 'base'),
    path('inputbarang/', views.Input_barang, name = 'inputbarang'),
    path('detail/<int:id_blog>', views.Detail, name = 'detail'),
]   