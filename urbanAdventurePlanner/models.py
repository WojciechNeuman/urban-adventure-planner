from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    epsg = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Route(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    path = models.TextField()
    length = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Route {self.pk} - Username: {self.user_id.username}. City: {self.city_id.name}"

class Point(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    index = models.IntegerField()
    description = models.TextField(max_length=200)
    address = models.CharField(max_length=200)
    epsg = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Point {self.pk} - {self.description}"