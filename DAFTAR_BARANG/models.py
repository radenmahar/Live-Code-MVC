from django.db import models

class DaftarBarang(models.Model):
    picture = models.CharField(max_length = 255)
    nama = models.CharField(max_length = 50)
    moto = models.TextField()
    harga = models.CharField(max_length = 50)