from django import template
from core.models import Usuario, Invite, Friend
from django.db.models import Q

register = template.Library()

@register.filter
def file_exists(file_):
    if not file_:
        return False
    return file_.storage.exists(file_.name)


@register.filter
def perfil_letter(name: str):
    return name[0].upper()

@register.filter
def check_friend(my_id, id):
    if my_id == id:
        return True
    return Friend.objects.filter(Q(user1_id__id=my_id, user2_id__id=id)|Q(user1_id__id=id, user2_id__id=my_id)).exists()