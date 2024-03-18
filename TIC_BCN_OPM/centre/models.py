from django.db import models

# Create your models here.
class Usuari(models.Model):
    ROLS = {
        "T": "Teacher",
        "S": "Student",
    }
    nom = models.CharField(max_length=30)
    cognoms = models.CharField(max_length=30)
    rol = models.CharField(max_length=30, choices=ROLS)
    correu = models.CharField(max_length=100)
    curs = models.CharField(max_length=30)
    moduls = models.CharField(max_length=30)