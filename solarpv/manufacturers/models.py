from django.db import models

class Manufacturer(models.Model):
    mName = models.CharField(max_length=100)
    registeredCountry = models.CharField(max_length=100)
    cName = models.CharField(max_length=100)


    def __str__(self):
        return self.mName
