from django.urls import path, include
from .views import login, logout, msg, test, search, invites, profile, signup, profile_user, post


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('signup/',signup, name='signup'),
    path('post/',post, name='post'),
    path('search/',search, name='search'),
    path('profile/',profile, name='profile'),
    path('profile/<int:pk>',profile_user, name='profile_user'),
    path('invites/<int:pk>/<int:invite>',invites, name='invites'),
    path('test/',test, name='test'),
    path('msg/<int:pk>',msg, name='msg'),
]