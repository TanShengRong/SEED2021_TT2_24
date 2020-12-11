from django.db import models

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
    custID = models.IntegerField()
    accountName = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    linked = models.BooleanField()

class TransactionAmounts(models.Model):
    senderID = models.IntegerField()
    receiverID = models.IntegerField()
    amount = models.FloatField()