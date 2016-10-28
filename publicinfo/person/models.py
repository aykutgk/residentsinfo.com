from django.db import models
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200, null=True, blank=True)
    facebook_full_name = models.CharField(max_length=200 ,null=True, blank=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, default=8052845564)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField()
    RACE = (
        ('W', 'White'),
        ('AA', 'African American'),
        ('A', 'Asian'),
        ('AI', 'American Indian')
    )
    race = models.CharField(max_length=2, choices=RACE)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.CharField(max_length=200)
    state = USStateField()
    city = models.CharField(max_length=50)
    zipcode = USZipCodeField()

    def __str__(self):
        return "{0} {1} {2}".format(self.first_name, self.middle_name, self.last_name)
