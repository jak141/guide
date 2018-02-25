from django.urls import path

from . import views

app_name = 'gazua'
urlpatterns = [
    path('', views.Index, name='index'),
    path('test/', views.Test, name='test'),
]
