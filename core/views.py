from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_
from .models import Usuario, Message, Friend, Invite, Post
from django.db.models import Q
import os

# Create your views here.

def test(request):
    context = {}
    return render(request, 'test.html',context)

@login_required(login_url="login")
def index(request):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    posts = Post.objects.all().order_by('-id')
    context['posts'] = posts
    return render(request, 'index.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'login.html',{})

def signup(request):
    return render(request, 'signup.html',{})

@login_required(login_url='login')
def logout(request):
    logout_(request)
    return redirect('index')

@login_required(login_url='login')
def msg(request, pk):
    context = {}
    context['pk'] = pk
    amigo_check = Friend.objects.filter(Q(user1_id=request.user, user2_id__id=pk)|Q(user1_id__id=pk, user2_id=request.user))
    if not amigo_check.exists():
        return redirect('index')
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    context['my_id'] = request.user.id
    return render(request, 'msg.html',context)

@login_required(login_url='login')
def search(request):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    return render(request, 'search.html',context)


@login_required(login_url='login')
def invites(request, pk, invite):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    context['my_id'] = request.user.id
    context['pk'] = pk
    context['invite'] = invite
    invite_check = Invite.objects.filter(id=invite)
    if not invite_check.exists():
        return redirect('index')
    return render(request, 'invites.html',context)

@login_required(login_url='login')
def profile(request):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name')
        user.description = request.POST.get('sobre')
        user.perfil_image = request.FILES.get('file_')
        user.save()
        if not user.perfil_image.height:
            os.remove(user.perfil_image.path)
            
    return render(request, 'profile.html',context)


@login_required(login_url='login')
def profile_user(request, pk):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    context['u'] = Usuario.objects.filter(id=pk).first()
    if request.user.id == pk:
        return redirect('index')
            
    return render(request, 'profile_user.html',context)


@login_required(login_url='login')
def post(request):
    context = {}
    amigos = Friend.objects.filter(Q(user1_id=request.user)|Q(user2_id=request.user))
    invites = Invite.objects.filter(Q(recv_user_id=request.user))
    context['amigos'] = amigos
    context['invites'] = invites
    if request.method == 'POST':
        user = request.user
        post = Post.objects.create(title=request.POST.get('title'),body=request.POST.get('body'), user_id=user, image=request.FILES.get('file_'))
        post.save()
        if not post.image.height:
            os.remove(post.image.path)
            post.delete()

        return redirect('index')
            
    return render(request, 'post.html',context)