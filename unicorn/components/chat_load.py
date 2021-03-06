from django_unicorn.components import UnicornView, PollUpdate
from core.models import Message
from django.db.models import Q

class ChatLoadView(UnicornView):
    pk = ''
    
    msgs = []
    
    my_id = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.my_id = self.request.user.id

    def mount(self):
        my_id = self.my_id
        self.msgs = Message.objects.filter(Q(recv_user_id=my_id, send_user_id=self.pk)|Q(recv_user_id__id=self.pk, send_user_id=my_id)).order_by('id')

    def get_msgs(self):
        my_id = self.my_id
        self.msgs = Message.objects.filter(Q(recv_user_id=my_id, send_user_id=self.pk)|Q(recv_user_id__id=self.pk, send_user_id=my_id)).order_by('id')
        return PollUpdate(timing=6000, disable=False, method="get_msgs")