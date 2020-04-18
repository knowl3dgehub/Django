import os
import binascii
from django.contrib.auth.models import AbstractUser
from django_mysql.models import JSONField
from django.conf import settings
from django.db import models

"""
Model for users registration
"""


class MyUser(AbstractUser):
    first_name = models.CharField(('name'), max_length=50)
    last_name = models.CharField(('lastname'), max_length=50)
    phone_number = models.CharField(('phone number'), null=True, max_length=10)
    age = models.CharField(('age'), null=True, max_length=3)
    created_at = models.DateTimeField(('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(('updated at'), auto_now=True)

    class Meta:
        db_table = "users"
