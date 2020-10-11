from django.contrib import admin
from .models import Problem, myUser, Problem_solutions

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')

admin.site.register(Problem_solutions)
admin.site.register(Problem)
admin.site.register(myUser, UserAdmin) 