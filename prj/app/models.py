from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.PositiveIntegerField(blank=True, null=True)
    death_year = models.PositiveIntegerField(blank=True, null=True)

    job = models.ForeignKey(
        'Job',
        on_delete=models.SET_NULL,
        null=True
    )

    workshop = models.ForeignKey(
        'Workshop',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Artwork(models.Model):
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=255, default="unknown")

    creator = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        null=True
    )

    gallery = models.ForeignKey(
        'Gallery',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name