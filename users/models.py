from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        # CREA Y DEVUELVE UN USUARIO CON LOS CAMPOS DADOS
        if not email:
            raise ValueError("Email address is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=True, unique=False)
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, unique=False)
    last_name = models.CharField(max_length=200, blank=False, unique=False)
    acronym_name = models.CharField(
        max_length=50, blank=False, unique=False, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name_plural = "Users"
        db_table = "Users"
        ordering = ("-id", )

    def save(self, *args, **kwargs) -> None:
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.acronym_name = f"{self.first_name[0]}{self.last_name[0]}"
        super().save(*args, **kwargs)
