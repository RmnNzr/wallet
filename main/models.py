from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    wallet = models.BigIntegerField(default=0)

    def __str__(self):
        return self.username


class Expense(models.Model):
    text = models.CharField(max_length=40)
    value = models.BigIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='expenses')

    def __str__(self):
        return "%s ---- %s" % (self.user, self.text)


class Income(models.Model):
    text = models.CharField(max_length=40)
    value = models.BigIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='incomes')

    def __str__(self):
        return "%s ---- %s" % (self.user, self.text)
