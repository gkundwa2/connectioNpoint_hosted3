from django import forms
from ConnectionApp.models import FamilyIdentity


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = FamilyIdentity
        fields = ['firstName', 'middleName',
                  'lastName', 'familyMembers', 'verified']
