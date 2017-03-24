from django.contrib import admin
from habito_app.models import Habit

# Pre-populate habit slug in admin page
class HabitAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	
admin.site.register(Habit, HabitAdmin)
