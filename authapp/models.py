from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from pathlib import Path
from time import time

# Create your models here.

def avatar_upload_path(instance, filename):
    return f"user_{instance.username}/avatar/{int(time()*1000)}{Path(filename).suffix}"

class PortalUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = ASCIIUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator], verbose_name = 'Username')
    first_name = models.CharField(max_length=150, blank=True, verbose_name = 'First name')
    last_name = models.CharField(max_length=150, blank=True, verbose_name = 'Last name')
    email = models.EmailField(unique=True, verbose_name = 'Email address')
    avatar = models.ImageField(upload_to = avatar_upload_path, blank = True, null=True, verbose_name = 'Portal user avatar')
    is_staff = models.BooleanField(default=False, verbose_name = 'Staff status')
    is_active = models.BooleanField(default=True, verbose_name = 'Active status')
    is_deleted = models.BooleanField(default = False, verbose_name = 'Deleted status')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Date created', editable = False)
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Date created', editable = False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def delete(self, *args):
        self.deleted = True
        self.save()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)