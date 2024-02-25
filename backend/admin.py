from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']

# Register your models here.
admin.site.register(User, UserAdmin)

