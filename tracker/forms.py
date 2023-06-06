from django import forms
from .models import Habit_Goal


class NewGoalForm(forms.ModelForm):
    class Meta:
        model = Habit_Goal
        fields = ('author', 'title', 'habit_type', 'goal_date',
                  'current_value', 'goal_date', 'description')
