from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    perfil_image = models.ImageField("Foto de Perfil!",blank=True, null=True, upload_to="profiles/")
    name = models.CharField("Nome",max_length=255, blank=True, null=True)
    description = models.TextField("Sobre", blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class Friend(models.Model):
    user1_id = models.ForeignKey('core.Usuario', related_name='user1_id_fr', on_delete=models.CASCADE)
    user2_id = models.ForeignKey('core.Usuario', related_name='user2_id_fr', on_delete=models.CASCADE)


class Invite(models.Model):
    recv_user_id = models.ForeignKey('core.Usuario', related_name='recv_user_id_inv', on_delete=models.CASCADE)
    send_user_id = models.ForeignKey('core.Usuario', related_name="send_user_id_inv", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)


class Message(models.Model):
    recv_user_id = models.ForeignKey('core.Usuario', related_name='recv_user_id_msg', on_delete=models.CASCADE)
    send_user_id = models.ForeignKey('core.Usuario', related_name="send_user_id_msg", on_delete=models.CASCADE)
    body = models.TextField('Message')

class Post(models.Model):
    user_id = models.ForeignKey('core.Usuario', related_name='user_id_post', on_delete=models.CASCADE)
    image = models.ImageField("Image!",blank=True, null=True, upload_to="posts/")
    title = models.CharField('Title', max_length=255)
    body = models.TextField('Text')


class Score(models.Model):
    user_id = models.ForeignKey('core.Usuario', related_name='user_id_score', on_delete=models.CASCADE)
    score = models.IntegerField('Score?')