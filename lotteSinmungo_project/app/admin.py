from django.contrib import admin
from .models import Problem, myUser, Solution

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')

admin.site.register(Solution)
admin.site.register(Problem)
admin.site.register(myUser, UserAdmin) 