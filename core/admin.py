from django.contrib import admin
from .models import Usuario, Message, Friend, Invite, Post


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',)