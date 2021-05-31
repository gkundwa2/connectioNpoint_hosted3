import django_filters
from .models import *


class FamilyFilter(django_filters.FilterSet):
    class Meta:
        model = FamilyIdentity
        fields = '__all__'
