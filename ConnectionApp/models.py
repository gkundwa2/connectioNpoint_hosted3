from django.db import models
# from phone_field import PhoneField

# Create your models here.


class FamilyIdentity(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50)
    familyMembers = models.PositiveIntegerField()
    # phone=models.PhoneField(blank=True, help_text='Contact Phone number')
    # email=models.EmailField(max_length=254)
    verified = models.BooleanField(default=False)
    # lastSeen=models.DateField(_(auto_now=False, auto_now_add=False)

    # class Meta:
    #     db_table=u'familyIdentity'

    def setVerified(self):
        self.verified = not self.verified
        self.save()

    def __str__(self):
        return self.firstName + " " + self.middleName + " " + self.lastName + " " + str(self.familyMembers) + " " + str(self.verified)


# + + self.phone + self.email
