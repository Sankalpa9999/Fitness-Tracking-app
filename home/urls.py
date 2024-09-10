from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('homepage/', views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('service/',views.service, name= 'service'),
    path('contact/',views.contact_page, name='contact'),

]