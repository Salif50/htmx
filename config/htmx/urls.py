from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('add/',views.add,name='add'),
    path('delete/<pk>/',views.delete,name='delete'),
    path('filtre/',views.filtre,name="filtre"),
]
