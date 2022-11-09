from django.db import models
from django.contrib.auth.models import AbstractUser
GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Undefined'),
)
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11,unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    province = models.CharField(max_length=200)
    email = models.EmailField()
    REQUIRED_FIELDS = []
    