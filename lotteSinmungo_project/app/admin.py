from django.contrib import admin
from .models import Problem, myUser, Solution,Photo
from django.contrib.auth.admin import UserAdmin

class PhotoInline(admin.TabularInline):
    model = Photo

# Register your models here.
admin.site.register(Photo)
admin.site.register(Solution)
admin.site.register(Problem)
admin.site.register(myUser, UserAdmin)