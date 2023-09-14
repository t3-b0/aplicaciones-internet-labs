from django.contrib import admin
from .models import Course, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','last_name', 'first_name', 'birth_date')

admin.site.register(Course)
admin.site.register(Student, StudentAdmin)