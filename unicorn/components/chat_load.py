from django_unicorn.components import UnicornView, PollUpdate
from core.models import Message
from django.db.models import Q

class ChatLoadView(UnicornView):
    pk = ''
    my_id = ''
    
    msgs = []

    def mount(self):
        self.msgs = Message.objects.filter(Q(recv_user_id=self.my_id)|Q(send_user_id=self.pk)|Q(recv_user_id__id=self.pk)|Q(send_user_id=self.my_id)).order_by('id')

    def get_msgs(self):
        self.msgs = Message.objects.filter(Q(recv_user_id=self.my_id)|Q(send_user_id=self.pk)|Q(recv_user_id__id=self.pk)|Q(send_user_id=self.my_id)).order_by('id')
        return PollUpdate(timing=4000, disable=False, method="get_msgs")