from django.db import models


class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True)
    species = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True)
    submitter = models.CharField(max_length=50)
    submission_date = models.DateField()
    description = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    vaccination = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

