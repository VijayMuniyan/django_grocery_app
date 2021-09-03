from django.urls import path
from Bag import views

urlpatterns = [

 path('home/', views.home, name='home'),
 path('registration/', views.registration, name='registration'),
 path('login/', views.login, name='login'),
 path('logout/', views.logout, name='logout'),
 path('add/', views.add, name='add'),
 path('details/', views.details, name='details'),
 path('update/<i>/', views.update, name='update'),
 path('last/', views.last, name='last'),



]
