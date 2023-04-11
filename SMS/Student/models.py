from django.db import models


class StudentModel(models.Model):
    rn = models.IntegerField(unique=True)
    fnm = models.CharField(max_length=30)
    lnm = models.CharField(max_length=30)
    mk = models.FloatField()

    def __str__(self) -> str:
        return f"{self.rn}"