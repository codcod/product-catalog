# pylint: disable=C0114,C0115,C0116
from django.db import models


class Journey(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    family = models.CharField(max_length=20)  # web, mobile, headless

    def __str__(self):
        return str(self.name)


class Feature(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    modelbank = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.journey.name}::{self.name}'


class SubFeature(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.feature.name}-{self.name}'


class Assignee(models.Model):
    journeys = models.ManyToManyField(Journey, blank=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    journeys = models.ManyToManyField(Journey, blank=True)

    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    journeys = models.ManyToManyField(Journey, blank=True)

    name = models.CharField(max_length=200)
    key = models.CharField(max_length=20)
    counter = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Vendor(models.Model):
    journeys = models.ManyToManyField(Journey, blank=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Version(models.Model):
    journeys = models.ManyToManyField(Journey, through='Release', blank=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Release(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.DO_NOTHING, blank=True, null=True)
    version = models.ForeignKey(Version, on_delete=models.DO_NOTHING, blank=True, null=True)

    release_date = models.DateField()
