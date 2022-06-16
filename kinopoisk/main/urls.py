from django.urls import path
from django.contrib.auth import views as vs
from . import views

urlpatterns = [
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path('enter', views.EnterView.as_view(), name='enter'),
    path('playlist', views.playlist, name='playlist'),
    path('registr', views.registr, name='registr'),
    path('kino/<int:pk>/edit/', views.UpdateFilms.as_view(), name='updatefilms'),
    path('kino/<int:pk>/delete/', views.DeleteFilms.as_view(), name='deletefilms'),
    path('logout/', views.user_logout, name='logout'),
    path('', vs.LoginView.as_view(), name='home'),
]
