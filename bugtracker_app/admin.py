from django.contrib import admin


# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Ticket



admin.site.register(Ticket)

class CustomUserAdmin(UserAdmin):
    model = MyUser

admin.site.register(MyUser, CustomUserAdmin)
