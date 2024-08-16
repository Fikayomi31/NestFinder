from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

"""Create a custom authentication backend to authenticate
users using their email"""


class EmailBackend(ModelBackend):
    """clas for email backend"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """Check the username/password and return a user"""
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user        
        return None
    
    def get_user(self, user_id):
        """Get user function"""
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
