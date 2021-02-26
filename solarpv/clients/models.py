from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    mName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipCode = models.CharField(max_length=10)
    officePhone = models.CharField(max_length=15)
    cellPhone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.fName + ' ' + self.lName
