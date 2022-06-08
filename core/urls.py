from django.urls import path, include
from .views import login, logout, msg, test, search, invites


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('search/',search, name='search'),
    path('invites/<int:pk>/<int:invite>',invites, name='invites'),
    path('test/',test, name='test'),
    path('msg/<int:pk>',msg, name='msg'),
]