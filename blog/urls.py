from django.urls import path
from . import views

# blog/
urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo)
]
