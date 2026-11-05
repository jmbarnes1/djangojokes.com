from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db import models
from django.urls import reverse

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')


class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    
    def get_absolute_url(self):
        return reverse('my-account') # Reverse returns a page starting from the destination and working backwards.

    avatar = models.ImageField(
        upload_to='avatars/', 
        blank=True,
        help_text='Image must be 200px by 200px.',
        validators=[validate_avatar]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'


"""
The AbstractUser class in Django provides a full user model with 11 default fields, allowing you to extend or replace them.  These fields are:

id: Auto-generated primary key.
password: Hashed password.
last_login: Timestamp of the last login.
is_superuser: Boolean indicating superuser status.
username: Unique string identifier (max 150 chars).
first_name: First name (max 150 chars, optional).
last_name: Last name (max 150 chars, optional).
email: Email address (optional by default).
is_staff: Boolean indicating staff/admin access.
is_active: Boolean indicating if the account is active. 
date_joined: Timestamp of account creation.
"""