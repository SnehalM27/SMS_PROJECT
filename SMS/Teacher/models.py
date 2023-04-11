from django.db import models

class TeacherModel(models.Model):
    tid = models.IntegerField(unique=True)
    fnm = models.CharField(max_length=30)
    lnm = models.CharField(max_length=30)
    sal = models.FloatField()

    def __str__(self) -> str:
        return f"{self.tid},{self.fnm},{self.lnm},{self.sal},"
