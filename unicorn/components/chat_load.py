from django_unicorn.components import UnicornView, PollUpdate
from core.models import Message
from django.db.models import Q

class ChatLoadView(UnicornView):
    polling_disabled = False
    msgs = []
    pk = ''
    my_id = ''

    def mount(self):
        self.msgs = Message.objects.filter(Q(recv_user_id=self.my_id)|Q(send_user_id=self.pk)|Q(recv_user_id__id=self.pk)|Q(send_user_id=self.my_id)).order_by('id')

    def get_msgs(self):
        self.msgs = Message.objects.filter(Q(recv_user_id=self.my_id)|Q(send_user_id=self.pk)|Q(recv_user_id__id=self.pk)|Q(send_user_id=self.my_id)).order_by('id')
        return PollUpdate(timing=2000, disable=self.polling_disabled, method="get_msgs")