from django_unicorn.components import UnicornView
from core.models import Invite, Friend, Usuario
from django.db.models import Q

from core.views import msg

class ProfileView(UnicornView):
    u=''
    my_id= ''
    is_friend=False
    msg = ''
    error=''

    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.my_id = self.request.user.id

    def mount(self):
        id = self.u.id
        check_invite = Invite.objects.filter(Q(recv_user_id__id=self.my_id, send_user_id__id=id)|Q(recv_user_id__id=id, send_user_id__id=self.my_id))
        if check_invite.exists():
            self.is_friend = True
            self.msg = 'Já existe uma solicitação pendente!'
            return

        check_friend = Friend.objects.filter(Q(user1_id__id=self.my_id, user2_id__id=id)|Q(user1_id__id=id, user2_id__id=self.my_id))

        if check_friend.exists():
            self.is_friend = True
            self.msg = 'Vocês já são amigos!'
            return

    def send(self):
        id = self.u.id
        check_invite = Invite.objects.filter(Q(recv_user_id__id=self.my_id, send_user_id__id=id)|Q(recv_user_id__id=id, send_user_id__id=self.my_id))
        if check_invite.exists():
            self.error = 'Já existe uma solicitação pendente!'
            return

        check_friend = Friend.objects.filter(Q(user1_id__id=self.my_id, user2_id__id=id)|Q(user1_id__id=id, user2_id__id=self.my_id))

        if check_friend.exists():
            self.error = 'Vocês já são amigos!'
            return

        send_user = Usuario.objects.filter(id=self.my_id).first()
        recv_user = Usuario.objects.filter(id=id).first()

        invite = Invite.objects.create(recv_user_id=recv_user,send_user_id=send_user)
        invite.save()