from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    name = models.CharField(max_length=15,blank=False,null=False)
    last_name = models.CharField(max_length=20,blank=False,null=False)
    age = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0,blank=False,null=False)
    email = models.EmailField()
    home = models.TextField(blank=False,null=True)

    def __str__(self):
        return "Es adoptado por {0}".format(self.name)
    
