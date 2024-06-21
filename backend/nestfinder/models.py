from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
import re


# Create your models here.
def validate_phone_number(value):
    if not re.match(r'^\+234\d{10}$', value):
        raise ValidationError("Phone number must start with +234 and be followed by exactly 10 digits.")

class User(models.Model):
    """ creating class for user """
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=14, validators=[validate_phone_number])  # +234 plus 10 digits
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    agent_number = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, validators=[validate_phone_number])  # +234 plus 10 digits

    def __str__(self):
        return self.agent_name
    

