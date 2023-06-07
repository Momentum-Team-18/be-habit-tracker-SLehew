from django.shortcuts import render, get_object_or_404, redirect
from .models import Tracker, Habit_Goal, User
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
        return redirect('goals-list')
    return render(request, 'tracker/goal_home.html', {'form': form})


def goal_list(request):
    habit_goals = Habit_Goal.objects.all()
    return render(request, 'tracker/goal_home.html', {'habit_goals': habit_goals})


def edit_goal(request, pk):
    goal = get_object_or_404(Habit_Goal, pk=pk)
    if request.method == 'GET':
        form = NewGoalForm(instance=goal)

    else:
        form = NewGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal-detail', pk=pk)
    return render(request, 'tracker/goal_edit.html', {'form': form})


def goal_home(request):
    user = get_object_or_404(User)
    goal = Habit_Goal.objects.all()
    context = {
        'user': user,
        'habit_goal': goal
    }
    return render(request, 'tracker/goal_home.html', context)
