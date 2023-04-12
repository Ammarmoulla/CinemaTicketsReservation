from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=50)
    hall = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie


class Guest(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name="reservation", on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name="reservation", on_delete=models.CASCADE)
