# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.functions import Substr, Concat
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import  Q, OuterRef, Exists
from django.utils import timezone



class UserQueryset(models.QuerySet):
    pass

class UserManager(BaseUserManager):
    use_in_migrations = True
    def get_queryset(self):
        return UserQueryset(self.model, using=self._db)

    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        groups = extra_fields.pop('groups', None)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if groups:
            user.groups.set(groups)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, TimestampedModel):
    """ first_name last_name email is_staff is_active date_joined """
    username    = None
    full_name   = models.GeneratedField(
        verbose_name=_("Nom et prenom"),
        expression=Concat('first_name', models.Value(' '), 'last_name'),
        output_field=models.CharField(max_length=100),
        db_persist=True
    )
    email       = models.EmailField(_('E-mail address'), unique=True)
    picture     = models.ImageField(upload_to='images/faces', null=True, blank=True)
    phone       = models.CharField(max_length=20, null=True, blank=True)
    address     = models.CharField(verbose_name=_("Address"), max_length=150, null=True, blank=True)

    is_manager  = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_prestataire = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    
        


