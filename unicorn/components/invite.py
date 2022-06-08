from django_unicorn.components import UnicornView
from core.models import Usuario, Invite, Friend
from django.shortcuts import redirect


class InviteView(UnicornView):
    my_id= ''
    pk = ''
    user= ''
    invite=""

    def mount(self):
        user = Usuario.objects.filter(id=self.pk).first()
        self.user = user


    def delete(self):
        inv = Invite.objects.filter(id=self.invite).first()
        inv.delete()
        return redirect('index')

    def aceitar(self):
        inv = Invite.objects.filter(id=self.invite).first()
        friend = Friend.objects.create(user1_id=inv.recv_user_id, user2_id=inv.send_user_id)
        friend.save()
        inv.delete()
        return redirect('index')