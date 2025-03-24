from django.urls import path
from . import views

urlpatterns = [
    path('', views.blank, name='blank'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('item/<str:item_id>/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
]