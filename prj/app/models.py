from django.db import models

class Person(models.Model):
    #id
    name = models.CharField(max_length=255)
    birth_year = models.PositiveSmallIntegerField(blank=True,null=True)
    death_year = models.PositiveSmallIntegerField(blank=True,null=True)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)
    teacher_workshop = models.ForeignKey('Workshop', on_delete=models.SET_NULL, null=True)

class Job(models.Model):
    #id
    name = models.CharField(max_length=255)

class Workshop(models.Model):
    #id
    name = models.CharField(max_length=255)
