from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Resident(models.Model):
    rid=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=12)
    address=models.CharField(max_length=256)
    email=models.EmailField(max_length=100)
    fathersname=models.CharField(max_length=30)
    occupation=models.CharField(max_length=12)
    vehiclenumber=models.CharField(max_length=11)
    idproof=models.CharField(max_length=11)
    rfid=models.CharField(max_length=11)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('residentdetail',kwargs={'pk':self.pk})


class Visitor(models.Model):
    resident=models.ForeignKey(Resident,on_delete=models.CASCADE)
    vid=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=12,)
    address_to_visit=models.TextField(max_length=256,)
    purpose_of_visit=models.CharField(max_length=500,)
    vehiclenumber=models.CharField(max_length=11,)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('visitordetail',kwargs={'pk':self.pk})


class Worker(models.Model):
    resident=models.ForeignKey(Resident,on_delete=models.CASCADE)
    wid=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=12)
    address=models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    status=models.CharField(max_length=10)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workerdetail',kwargs={'pk':self.pk})

class Company(models.Model):
    cid=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companydetail',kwargs={'pk':self.pk})


class Delivery(models.Model):
    did=models.CharField(max_length=10,primary_key=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    resident=models.ForeignKey(Resident,on_delete=models.CASCADE)
    vehiclenumber=models.CharField(max_length=11)
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('deliverydetail',kwargs={'pk':self.pk})
