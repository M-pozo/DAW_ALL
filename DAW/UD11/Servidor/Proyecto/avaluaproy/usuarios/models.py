from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# Create your models here.
#UD8.1.b BEGIN
class MyUserManager(BaseUserManager):
    def create_user(
            self, email, first_name=None, last_name=None, password=None, type=None
        ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=33, null=True)
    email = models.EmailField(_('email address'), unique=True)
    activo = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
#UD8.1.b END