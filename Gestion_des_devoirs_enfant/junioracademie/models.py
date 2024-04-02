from django.db import models

# Create your models here.

class Enfant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    niveau_scolaire = models.CharField(max_length=255)
    adresse = models.TextField()  
    parent_tuteur = models.CharField(max_length=100)

class Enseignant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    qualifications = models.TextField()

class Classe(models.Model):
    nom = models.CharField(max_length=255)
    niveau_scolaire = models.CharField(max_length=255)
    nombre_enfants = models.IntegerField()

class Cours(models.Model):
    matiere = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    duree = models.IntegerField()
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
