from django.urls import path

from . import views

app_name = 'gazua'
urlpatterns = [
    path('', views.Index, name='index'),
    path('test/', views.Test, name='test'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('guide_write/', views.Guide_Write, name='guide_write'),
]
