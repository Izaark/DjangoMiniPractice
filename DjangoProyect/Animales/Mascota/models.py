from __future__ import unicode_literals

from django.db import models
from Adopccion.models import Persona

class Vacuna(models.Model):
	name = models.CharField(max_length=25,blank=False, null=False)
	def __str__(self):
		return self.name
class Mascota(models.Model):

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        #Attrubutes
    #ssfolio = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=15,blank=False,null=False)
    sex = models.CharField(max_length=20,blank=False,null=False)
    age = models.IntegerField(default=0)
    date = models.DateField()

    #Reltions
    persona = models.ForeignKey(Persona, null=False,blank=False, on_delete=models.CASCADE)
    vacuna= models.ManyToManyField(Vacuna)


    def __str__(self):
        return "Hola {0}".format(self.name)
    
