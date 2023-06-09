from django.contrib import admin
from .models import User, Habit_Goal, Tracker

admin.site.register(User)
admin.site.register(Habit_Goal)
admin.site.register(Tracker)
