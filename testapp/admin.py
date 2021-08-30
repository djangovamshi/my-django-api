from django.contrib import admin

# Register your models here.
from testapp.models import StudentResult

class StudentResultAdmin(admin.ModelAdmin):
    list_display=['id','roll_number','name','dob','marks']


admin.site.register(StudentResult,StudentResultAdmin)
