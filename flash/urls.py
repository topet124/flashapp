from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('divide', views.divide, name="divide"),
    path('multiply', views.multiply, name="multiply"),
    path('subtract', views.subtract, name="subtract"),
    path('add', views.add, name="add"),
]
