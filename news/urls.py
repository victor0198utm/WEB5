from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add, name='add_news'),
    path('<slug:slug>/update', views.update),
    path('<slug:slug>/', views.detail, name='news_detail'),
]
