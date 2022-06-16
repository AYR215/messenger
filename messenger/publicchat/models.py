from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublicChat(models.Model):
    name = models.CharField(max_length=200, null=False, primary_key=True, unique=True)

    def __str__(self):
        return self.name


#class PublicMessage(models.Model):
#    chat = models.ForeignKey(PublicChat)
#    author = models.ForeignKey(User)
#    message = models.TextField
#    pub_date = models.DateTimeField(default=timezone.now)
#    is_readed = models.BooleanField(default=False)

#    class Meta:
#        ordering = ['pub_date']
#
#    def __str__(self):
#        return self.message
