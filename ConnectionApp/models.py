from django.db import models
import datetime


class FamilyIdentity(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50)
    familyMembers = models.PositiveIntegerField()
    phone = models.CharField(blank=True, null=True, max_length=20)
    verified = models.BooleanField(default=False)
    national_doc = models.CharField(null= True, blank=True, max_length=30)


    def setVerified(self):
        self.verified = not self.verified
        self.save()

    def __str__(self):
        return self.firstName + " " + self.middleName + " " + self.lastName + " " + str(self.familyMembers) + " " + str(self.verified)


class Transaction(models.Model):
    """ model which represents an abstraction of transactions in the database ."""

    family = models.ForeignKey(FamilyIdentity, related_name="family_transactions", on_delete=models.CASCADE)
    trans_date = models.DateTimeField(default=datetime.datetime.now)
    food_given = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.trans_date}"
