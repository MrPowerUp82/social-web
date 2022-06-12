from django_unicorn.components import UnicornView
from core.models import Message, Usuario
from django import forms
import time

class ChatMsgForm(forms.Form):
    text = forms.CharField(max_length=255, required=True)


class ChatMsgView(UnicornView):

    text = ''

    pk = ''

    my_id = ''

    loading = False

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.my_id = self.request.user.id


    def send(self):
        if self.is_valid() and self.text != '':
            self.loading = True
            my_id = self.my_id
            send_user = Usuario.objects.filter(id=my_id).first()
            recv_user = Usuario.objects.filter(id=self.pk).first()
            msg = Message.objects.create(recv_user_id=recv_user, send_user_id=send_user, body=self.text)
            msg.save()
            self.text =''
            self.loading = False

