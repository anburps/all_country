from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    geoname_id = models.IntegerField(unique=True)

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
