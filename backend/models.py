from django.db import models
from django.db.models import Sum
from User_Account_API.basemodel import TimeBaseModel
from django.utils.translation import gettext_lazy as _
# from .utils import generate_six_random_numbers, send_raw_email
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomerUserManager
# Create your models here.


class User(AbstractUser):
    username      = None
    email         = models.EmailField(_('email address'), unique=True)
    date_joined   = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD =  "email"
    REQUIRED_FIELDS = []

    objects = CustomerUserManager()

    def __str__(self):
        return self.email if self.email else ""


# class UserEmailVerification(TimeBaseModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=6, blank=True, null=True)
#     is_verified = models.BooleanField(default=False)
    
#     def save(self, *args, **kwargs):
#         if not self.code:
#             self.code = generate_six_random_numbers()
#         super().save(*args, kwargs)

#     def __str__(self) -> str:
#         return self.user.email    