from django.contrib.auth import get_user_model
from django.db import models


class TypeBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True


class ProcedureType(TypeBase):
    icon = models.ImageField(default='images/doctor.svg')
    icon_pink = models.ImageField(default='images/doctor_pink.svg')


class NoteType(TypeBase):
    icon = models.ImageField(default='images/pill.svg')
    icon_birch = models.ImageField(default='images/pill_birch.svg')


# class Procedure(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=128, unique=True)
#     frequency = models.DurationField()
#     start_date = models.DateField()
#     ptype = models.ForeignKey(ProcedureType, models.CASCADE)


class EntryBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date_time = models.DateTimeField()
    comment = models.TextField(null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Appointment(EntryBase):
    address = models.CharField(max_length=255)
    ptype = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)


class Note(EntryBase):
    ntype = models.ForeignKey(NoteType, on_delete=models.CASCADE)


