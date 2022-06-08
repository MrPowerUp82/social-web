from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_
from .models import Usuario, Message, Friend, Invite
from django.db.models import Q

# Create your views here.

def test(request):
    context = {}
    return render(request, 'test.html',context)

@login_required(login_url="login")
def index(request):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    context['amigos'] = amigos
    return render(request, 'index.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'login.html',{})

@login_required(login_url='login')
def logout(request):
    logout_(request)
    return redirect('index')

@login_required(login_url='login')
def msg(request, pk):
    context = {}
    context['pk'] = pk
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    context['amigos'] = amigos
    context['my_id'] = request.user.id
    return render(request, 'msg.html',context)    
