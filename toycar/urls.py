from django.urls import path
from . import views

urlpatterns = [
    path('', views.blank, name='blank'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('auth/complete/google-oauth2/<str:state>', views.auth_google_oauth2, name='auth_google_oauth2'),
    path('logout/', views.logout_view, name='logout'),
    path('item/<str:item_id>/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
    path('settings/', views.settings, name='settings'),
    path('classic/', views.classic, name='classic'),
    path('speed/', views.speed, name='speed'),
    path('offroad/', views.offroad, name='offroad'),
    path('contact/', views.contact, name='contact'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('faq/', views.faq, name='faq'),
    path('care/', views.care, name='care'),
    path('test-email/', views.test_email, name='test_email'),
    path('test-firebase/', views.test_firebase, name='test_firebase'),
    path('ordered/', views.ordered, name='ordered'),
    path('deletedata/', views.deletedata, name='deletedata'),
]