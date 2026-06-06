from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["phone_number"],
                condition=Q(phone_number__isnull=False),
                name="unique_phone_number_when_present",
            )
        ]
