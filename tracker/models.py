from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, null=True)


class Habit_Goal(models.Model):
    RELATIONSHIPS = 'R'
    FITNESS_WELLNESS = 'FW'
    WORKPLACE = 'W'

    HABIT_TYPE = [
        (RELATIONSHIPS, 'Relationships'),
        (FITNESS_WELLNESS, 'Fitness_Wellness'),
        (WORKPLACE, 'Workplace'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_type = models.CharField(max_length=50, choices=HABIT_TYPE)
    current_value = models.IntegerField(blank=True, null=True)
    goal_value = models.IntegerField(blank=True, null=True)
    goal_date = models.DateField()
    post_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=400)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Tracker(models.Model):
    check_in_date = models.DateField(default=datetime.date.today)
    updated_value = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    goal = models.ForeignKey(Habit_Goal, on_delete=models.CASCADE)
