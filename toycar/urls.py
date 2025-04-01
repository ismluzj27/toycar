from django.urls import path
from . import views

urlpatterns = [
    path('', views.blank, name='blank'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('item/<str:item_id>/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
    path('settings/', views.settings, name='settings'),
    path('classic/', views.classic, name='classic'),
    path('speed/', views.speed, name='speed'),
    path('offroad/', views.offroad, name='offroad'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('care/', views.care, name='care'),
]