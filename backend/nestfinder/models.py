from django.db import models
from django.contrib.auth.models import AbstractUser
from .mixins import PhoneNumberValidatorMixin


class CustomUser(AbstractUser):
    """Creating a custom user"""
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('agent', 'Agent'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )
    def save(self, *args, **kwargs):
        if self.user_type == 'customer':
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class CustomerProfile(models.Model, PhoneNumberValidatorMixin):
    """Creating profile for customer"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='customer_profiles/', blank=True, null=True)
    phone = models.CharField(max_length=15, default='0000000000')

    def __str__(self):
        return f"{self.user.username} - Customer"
    
    def clean(self):
        super().clean()
        self.validate_phone_number()


class AgentProfile(models.Model, PhoneNumberValidatorMixin):
    """Creating profile for agent"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    licence_number = models.CharField(max_length=50)
    agency_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='0000000000')
    profile_picture = models.ImageField(upload_to='agent_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Agent"
    
    def clean(self):
        super().clean()
        self.validate_phone_number()
    

class Property(models.Model):
    """Creating class for property"""
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    PROPERTY_TYPE_CHOICES = [
        ('rental', 'Rental'),
        ('sale', 'Sale'),
    ]
    type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    available_from = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        permissions = [
            ("can_manage_property", "Can manage property"),
        ]

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='property_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"


class SavedSearch(models.Model):
    """Class for saved searches"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    search_criteria = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saved search by {self.user.username}"


class Message(models.Model):
    """Class for messages"""
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"


class Review(models.Model):
    """Class for reviews"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.agent.user.username}"


class Transaction(models.Model):
    """Class for transactions"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Transaction of {self.amount} by {self.user.username}"
