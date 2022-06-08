from django.urls import path, include
from .views import login, logout, msg, test


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('test/',test, name='test'),
    path('msg/<int:pk>',msg, name='msg'),
]