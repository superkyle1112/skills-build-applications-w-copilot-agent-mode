# Users, Teams, Activities, Leaderboard, Workouts models
from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

	def __str__(self):
		return f"{self.name} ({self.email})"

class Activity(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	date = models.DateField()
	points = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.name} - {self.user.name}"

class Workout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='workout_activities')
	duration = models.IntegerField(help_text='Duration in minutes')
	calories = models.IntegerField(default=0)
	date = models.DateField()

	def __str__(self):
		return f"Workout for {self.user.name} on {self.date}"

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
	total_points = models.IntegerField(default=0)
	rank = models.IntegerField(default=0)

	def __str__(self):
		return f"Leaderboard: {self.team.name} (Rank {self.rank})"
