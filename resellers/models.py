from django.db import models
from django.contrib.auth.models import AbstractUser


class Reseller(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cpf = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Revendedor'
        verbose_name_plural = 'Revendedores'

    def __str__(self):
        return self.email
