from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomerProfile, AgentProfile, Property
from .models import  PropertyImage, SavedSearch, Message, Review, Transaction

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile)
admin.site.register(AgentProfile)
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(SavedSearch)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(Transaction)
