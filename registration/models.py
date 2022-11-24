from django.db import models

# Create your models here.
from django.db import models


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    geb = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    memberNr = models.CharField(max_length=200, default="not a member")
    food = models.CharField(max_length=200,  default="")


class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Seminar(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)


class Participant2Seminar(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    pref = models.CharField(max_length=200, default="")


