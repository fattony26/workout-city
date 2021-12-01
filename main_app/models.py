from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

DIDYOU =  (
    ('Y', 'Yes'),
    ('N', 'No')
)

class Workout(models.Model):
    muscle_grp = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.muscle_grp

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={'workout_id': self.id})

class DidWorkout(models.Model):
    date = models.DateField()
    did_workout = models.CharField(
        max_length=1,
        choices=DIDYOU,
        default=DIDYOU[0][0]
        )
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_did_workout_display()} on {self.date}"
        
    