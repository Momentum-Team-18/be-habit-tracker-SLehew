from django import forms
from .models import Habit_Goal, Tracker


class NewGoalForm(forms.ModelForm):
    class Meta:
        model = Habit_Goal
        fields = ('author', 'title', 'habit_type', 'goal_date',
                  'current_value', 'goal_date', 'description')


class NewTrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('check_in_date', 'todays_value', 'notes', 'goal')
