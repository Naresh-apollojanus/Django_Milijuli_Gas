from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client


# Create your models here.
class AddField(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    address = models.TextField(max_length=20)


class Sms(models.Model):
    results = models.TextField()

    def __str__(self):
        return str(self.results)

    def save(self, *args, **kwargs):
        # account_sid = 'AC5cfcfa5f9996a1dc6dc5b18f8134ea00'
        # auth_token = '73787a9734a4d4857a65489dd5a67702'
        account_sid = 'AC5cfcfa5f9996a1dc6dc5b18f8134ea00'
        auth_token = '73787a9734a4d4857a65489dd5a67702'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'{self.results}',
            from_=' +13156403550',
            to='+9779847450466'
        )

        print(message.sid)

        # +13156403550

        return super().save(*args, **kwargs)


# 794tA4ugDxvZJKJcasL1PTwRw6xmindLGj_xYa3R(damudada phone)
class Order(models.Model):
    username = models.CharField(max_length=30)
    choose_cylinder = models.CharField(max_length=30,null=True)
    qty = models.IntegerField()
    time = models.CharField(null=True, max_length=30)
    path_name = models.CharField(null=True, max_length=30)
