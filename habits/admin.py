from django.contrib import admin

from habits.models import Habit


# Register your models here.
@admin.register(Habit)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["action"]