from django.db import models

# Create your models here.
class Modeller(models.Model):
    titel = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu_images/')
    beskrivelse = models.TextField()
    tilbehør = models.TextField(max_length=100)

    def __str__(self):
        return self.titel

class Kategori(models.Model):
    titel = models.CharField(max_length=50)

    def __str__(self):
        return self.titel
