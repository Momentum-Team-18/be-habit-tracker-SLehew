from django.shortcuts import render, get_object_or_404, redirect
from .models import Tracker, Habit_Goal
from .forms import NewGoalForm


def tracker_home(request):
    trackers = Tracker.objects.all()
    return render(request, 'tracker/tracker_home.html', {'trackers': trackers})


def new_goal(request):
    if request.method == 'GET':
        form = NewGoalForm()
    else:
        form = NewGoalForm(request.POST)
        form.save()
        return redirect('tracker-home')
    return render(request, 'tracker/new_goal.html', {'form': form})
