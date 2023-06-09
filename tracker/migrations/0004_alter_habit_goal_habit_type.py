# Generated by Django 4.2.2 on 2023-06-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_habit_goal_habit_type_delete_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit_goal',
            name='habit_type',
            field=models.CharField(choices=[('R', 'Relationships'), ('FW', 'Fitness_Wellness'), ('W', 'Workplace')], max_length=50),
        ),
    ]
