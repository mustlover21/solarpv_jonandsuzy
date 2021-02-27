from django.db import models

class Product(models.Model):
    manufacturer = models.CharField(max_length=100)
    modelNumber = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    totalnumofCells = models.CharField(max_length=100)
    numberofseriesStrings = models.CharField(max_length=100)
    seriesfuseRating = models.CharField(max_length=100)
    frameType = models.CharField(max_length=100)
    maxVoltage = models.CharField(max_length=100)
    voc = models.CharField(max_length=100)
    isc = models.CharField(max_length=100)
    vmp = models.CharField(max_length=100)
    imp = models.CharField(max_length=100)
    pmp = models.CharField(max_length=100)
    ff = models.CharField(max_length=100)


    def __str__(self):
        return self.manufacturer + ' ' + self.modelNumber
