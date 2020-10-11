from django.contrib import admin
from .models import Problem, myUser

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')


admin.site.register(Problem)
admin.site.register(myUser, UserAdmin) 