# Generated by Django 4.2.2 on 2023-06-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_genre_tracker_habit_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit_goal',
            name='habit_type',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]