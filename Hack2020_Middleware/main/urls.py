from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('register_vessel', views.register_vessel, name='register_vessel'),
    path('loginHome', views.loginHome, name='loginHome'),
    path('login_view', views.login_view, name='login_view'),
    path('home', views.home_view, name='home_view'),
    path('logout', views.logOut, name='logOut'),
    path('vessels', views.vessels_view, name='vessels_view'),
    path('<int:vessel_id>/details', views.vessel_details, name='vessel_details'),
    path('home/weatherFinder', views.weatherFinder, name='weatherFinder'),
    #path('home/<int:lat>/<int:lng>', views.psnFinder, name='psnFinder'),
   # path('voyage_view', views.voyage_view, name='voyage_view'),

]
