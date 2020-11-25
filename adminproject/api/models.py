from django.db import models

# Create your models here.
class EmployerTask(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=25)
    ph_no= models.CharField(max_length=13,unique=True)
    password = models.CharField(max_length=50)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title