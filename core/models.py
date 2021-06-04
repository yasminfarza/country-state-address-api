from django.db import models


class Country(models.Model):
    """"Country object"""
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    code = models.CharField(max_length=50)

    class Meta:
        unique_together = ("latitude", "longitude")

    def __str__(self):
        return self.name


class State(models.Model):
    """"State object"""
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    """"Address object"""
    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50, null=True)
    road_number = models.IntegerField(null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
