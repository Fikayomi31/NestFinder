""" Creating a signal file that create a profile when a
user is created and save the profile when a user is saved
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, CustomerProfile, AgentProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """create user profile"""
    if created:
        if instance.user_type == 'customer':
            CustomProfile.objects.create(user=instance)
        elif instance.user_type == 'agent':
            AgentProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """saving user"""
    if instance.user_type == 'customer':
        instance.customerprofile.save()
    elif instance.user_type == 'agent':
        instance.agentprofile.save()
