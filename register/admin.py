from django.contrib import admin
from .models import UserDetails, UserAddresses


# Register your models here.
@admin.register(UserDetails)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password')

@admin.register(UserAddresses)
class UserAddressesAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'city', 'state', 'pincode', 'country')




