from django.db import models

# Create your models here.
class StudentModel(models.Model):
    rn = models.IntegerField(unique=True)
    fnm = models.CharField(max_length=30)
    lnm = models.CharField(max_length=30)
    mk = models.FloatField()