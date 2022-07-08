import datetime
from django.core import validators
from django.db import models

# Create your models here.
class Actor(models.Model):
    firstname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    lastname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    date_of_birth = models.DateField(validators=[validators.MaxValueValidator(limit_value=datetime.date.today())])
    MALE = 'M'
    FEMALE = 'F'
    YEAR_IN_SCHOOL_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Director(models.Model):
    firstname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    lastname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    date_of_birth = models.DateField(validators=[validators.MaxValueValidator(limit_value=datetime.date.today())])
    MALE = 'M'
    FEMALE = 'F'
    YEAR_IN_SCHOOL_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Character(models.Model):
    firstname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    lastname = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r'[a-zA-Z]+', message='Please use only letters A-Z')])
    actor = models.ForeignKey(to=Actor, on_delete=models.PROTECT, )

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Movie(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, validators=[validators.RegexValidator(regex=r"[a-zA-Z0-9- '`(){}[]&]+", message='Please use only letters A-Z, numbers and special characters')])
    release_date = models.DateField(validators=[validators.MaxValueValidator(limit_value=datetime.date.today())])
    characters = models.ManyToManyField(Character)
    director = models.ForeignKey(to=Director, on_delete=models.PROTECT, )
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[validators.MinValueValidator(limit_value=0.0), validators.MaxValueValidator(limit_value=10.0)])

    def __str__(self):
        return f'{self.name}'


