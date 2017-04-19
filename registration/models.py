from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
