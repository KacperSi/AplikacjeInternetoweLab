from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django import forms

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),    
        )

class Mentor(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default = 'Male')
    date_of_birth = models.DateField(default=date.today)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class TeamUser(AbstractUser):
    team_name = models.CharField(max_length = 40)
    school = models.CharField(max_length = 100)
    guardian_consent = models.BooleanField()
    participant_1 = models.CharField(max_length = 100)
    participant_2 = models.CharField(max_length = 100)
    participant_3 = models.CharField(max_length = 100)
    participant_4 = models.CharField(max_length = 100)
    participant_5 = models.CharField(max_length = 100)

    def create_user(team_name, school):
        user = TeamUser()
        user.set_unusable_password()
        user.save()
        return user
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"