from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('enter', views.enter, name='enter'),
    path('playlist', views.playlist, name='playlist'),
    path('registr', views.registr, name='registr'),
    path('kino/<int:pk>/edit/', views.UpdateFilms.as_view(), name='updatefilms'),
    path('kino/<int:pk>/delete/', views.DeleteFilms.as_view(), name='deletefilms'),
]
