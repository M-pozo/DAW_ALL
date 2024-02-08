from django.contrib import admin
from .models import MyUser

# Register your models here.

#UD8.1.c BEGIN
class MyUserAdmin(admin.ModelAdmin):
    list_display = list_display_link = ('username', 'email', 'activo', 'is_staff', 'is_active')
    search_fields = ['username', 'email']
    ordering = ['email']

admin.site.register(MyUser, MyUserAdmin)
#UD8.1.c END
