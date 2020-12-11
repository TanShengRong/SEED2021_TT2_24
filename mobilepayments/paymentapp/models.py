from django.db import models
import datetime

class ModelName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete = models.CASCADE)

    def __str__(self):
        return self.name 

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name 

class UserDetails(models.Model):
    custID = models.IntegerField()
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    nric = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    accountName = models.CharField(max_length=50)

class AccountDetails(models.Model):
    username = models.CharField(max_length=50)
    accountName = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    linked = models.BooleanField()
    balance = models.FloatField()

class TransactionAmounts(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)