from django.contrib import admin
from .models import Category,Course,Course_Module,Course_Video

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Course_Module)
admin.site.register(Course_Video)