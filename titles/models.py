from django.db import models

# Create your models here.
class Numeric(models.Model):
    alias=models.CharField(max_length=50,unique=True)
    number=models.SmallIntegerField(default=0)
    def __str__(self):
        return self.alias
    class Meta():
        verbose_name="User"

class Sample2(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
    class Meta():
        verbose_name="Sample2"