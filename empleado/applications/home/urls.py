from django.urls import path
from . import views

urlpatterns = [
     path(
          '', 
          views.InicioView.as_view(),
          name = 'inicio'
     ),
     path('home2/', views.IndexView.as_view()),
     path('lista/', views.PruebaListView.as_view()),
     path('lista-prueba', views.ModeloPruebaListView.as_view()),
     path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
     path(
          'resume-foundation/',
          views.ResumeFoundationView.as_view(),
          name='resume_foundation'
     ),
     path(
          'home1/',
          views.PruebaHome1View.as_view(),
          name='home1'
     ),
     path(
          'home2p/',
          views.PruebaHome2View.as_view(),
          name='home2'
     ),
     path(
          'home3/',
          views.PruebaHome3View.as_view(),
          name='home3'
     ),
]