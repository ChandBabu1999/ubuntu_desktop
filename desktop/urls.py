from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-action/', views.menu_action, name='menu_action'),
]