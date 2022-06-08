from django_unicorn.components import UnicornView, PollUpdate
from datetime import datetime


class TodoView(UnicornView):
    task = ''
    tasks = []

    def add_task(self):
        self.tasks.append(self.task)

    def delete_task(self,t):
        self.tasks.remove(t)
