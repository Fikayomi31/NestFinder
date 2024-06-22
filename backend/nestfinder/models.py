"""creating models"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Creating a custom user"""
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('agent', 'Agent'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


class CustomerProfile(models.Model):
    """creating profile for customer"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class AgentProfile(models.Model):
    """creating profile for agent"""
    user = models.OnToOneField(CustomUser, on_delete=models.CASCADE)
    licence_number = models.CharField(max_length=50)
    agency_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_yo='agent_profiles/', blank=True, null=True)

class Property(models.Model):
    """creating class for property"""
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=200, decimal_places=2)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    PROPERTY_TYPE_CHOICES = [('rental', 'Rental'),
            ('sale', 'Sale'),
            ]
    type = models.CharField(max_length=10, choicee=PROPERTY_TYPE_CHOICES)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    available_from = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='property_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class SavedSearch(models.Model):
    """class for search models"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    search_criteria = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Models):
    """class for message"""
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class Review(models.Model):
    """class for review"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    """class for transaction"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
