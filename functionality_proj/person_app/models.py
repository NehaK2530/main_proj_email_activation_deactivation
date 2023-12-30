from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    GENDER = [('male','male'),('female','female'),('other','other')]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=23)
    gender = models.CharField(max_length=10, choices=GENDER)
    city= models.CharField(max_length=20)
    contact_no = PhoneNumberField(null=False, blank=True, unique=True, region='IN')
    aadhar_card_no = models.IntegerField()
    email = models.EmailField(max_length=50)
