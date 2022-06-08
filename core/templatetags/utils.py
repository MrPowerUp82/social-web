from django import template

register = template.Library()

@register.filter
def file_exists(file_):
    if not file_:
        return False
    return file_.storage.exists(file_.name)


@register.filter
def perfil_letter(name: str):
    return name[0].upper()