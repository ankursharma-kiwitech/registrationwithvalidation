from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserDetails(AbstractBaseUser):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=160)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'username', 'password']

    def __str__(self):
        return self.username


class UserAddresses(models.Model):
    useradd = models.ForeignKey(UserDetails, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['address', 'city', 'state', 'pincode', 'country']

    def __str__(self):
        return self.address


