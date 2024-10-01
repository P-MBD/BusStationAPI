from django.db import models

class Station(models.Model):
    Title = models.CharField(max_length=255)
    English_title = models.CharField(max_length=255)
    Line = models.CharField(max_length=50)
    Address = models.TextField()
    Lat = models.FloatField()
    Lang = models.FloatField()
    Description = models.TextField()

    def __str__(self):
        return self.title

class Information(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='information')
    day = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.station.title} - {self.day}"
