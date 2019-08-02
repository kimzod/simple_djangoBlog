from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
