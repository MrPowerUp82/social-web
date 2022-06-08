from django.utils.timezone import now
from django_unicorn.components import PollUpdate, UnicornView

class PollUpdateView(UnicornView):
    polling_disabled = False
    time = now().strftime('%H:%M:%S')

    def get_date(self):
        self.time = now().strftime('%H:%M:%S')
        return PollUpdate(timing=1000, disable=False, method="get_date")