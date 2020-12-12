from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    def __str__(self):
        return self.username


class Car(models.Model):
    car_name = models.CharField(_('car name'), max_length=100)
    description = models.TextField(_('description'), default='')
    license_plate_number = models.CharField(_('license plate'),
                                            max_length=15,
                                            unique=True,
                                            blank=False)
    owner = models.ForeignKey(to=User, related_name='cars', on_delete=models.CASCADE)
