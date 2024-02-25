from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create User with the given email and password
        
        """
        if not email:
            raise ValueError(_("The email must be set."))

        if "@" and ".com" not in email:
            raise ValueError(_("The email must contain @ and .com"))

        user = self.model(email=self.normalize_email(email), **extra_fields) 
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create Superuser with the given email and password

        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
