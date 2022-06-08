from django_unicorn.components import UnicornView
from core.models import Message, Usuario
from django import forms

class ChatMsgForm(forms.Form):
    text = forms.CharField(max_length=255, required=True)


class ChatMsgView(UnicornView):

    my_id = ''

    text = ''

    pk = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)


    def send(self):
        if self.is_valid():
            send_user = Usuario.objects.filter(id=self.my_id).first()
            recv_user = Usuario.objects.filter(id=self.pk).first()
            msg = Message.objects.create(recv_user_id=recv_user, send_user_id=send_user, body=self.text)
            msg.save()
            self.text =''

