from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    cumpleanos=models.DateField()
    
    def __str__(self):
        return self.nombre +' '+str(self.edad)+' '+str(self.cumpleanos)
    