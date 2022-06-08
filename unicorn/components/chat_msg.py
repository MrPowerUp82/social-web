from django_unicorn.components import UnicornView
from core.models import Message


class ChatMsgView(UnicornView):

    my_id = ''

    text = ''

    pk = ''

    def send(self):
        print('iai')
        if self.text != '':
            msg = Message.objects.create(recv_user_id__id=self.friend_id, send_user_id__id=self.my_id, body=self.text)
            msg.save()
            self.text =''

