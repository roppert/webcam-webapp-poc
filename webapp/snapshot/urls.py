from django.urls import path
from snapshot import views

urlpatterns = [
    path('', views.main, name='main'),
    path('upload', views.upload, name='upload'),
]
