from django_unicorn.components import UnicornView
from core.models import Usuario, Invite, Friend
from django.db.models import Q

class SearchView(UnicornView):
    search= ''

    my_id = ''

    error = ""

    def users(self):
        if len(self.search) >= 3:
            return [x for x in Usuario.objects.all().exclude(id=self.my_id) if self.search.lower() in x.name.lower() or self.search.lower() in x.username.lower()]


    def send(self,id):
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