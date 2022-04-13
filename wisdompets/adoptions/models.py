from django.db import models


class Pet(models.Model):
	SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
	name = models.Charfield(max_length=100)
	submitter = models.Charfield(max_length=100)
	species = models.Charfield(max_length=30)
	breed = models.Charfield(max_length=30, blank=True)
	description = models.TextField()
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
	submission_date = models.DateTimeField()
	age = models.IntegerField(null=True)
	vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
	name = models.Charfield(max_length=50)
