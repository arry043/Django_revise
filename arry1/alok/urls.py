from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_alok, name='all_alok'),
    path('<int:id>/', views.alok_detail, name='alok_detail'),
    path('add_alok/', views.add_alok_view, name='add_alok'),
]
