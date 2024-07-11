from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
 
# = == == == == ==================================================================
 
# from django.contrib.auth.admin import UserAdmin

# # from .models import CustomUser

# admin.site.register(CustomUser, UserAdmin)

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']  # Customize the fields displayed in the admin list view

admin.site.register(UserProfile, UserProfileAdmin)

 

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'is_staff', 'is_active',)
#     list_filter = ('is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password', 'conform_password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    # search_fields = ('username', 'password',)
    # ordering = ('username',)

# admin.site.register(CustomUser, CustomUserAdmin)