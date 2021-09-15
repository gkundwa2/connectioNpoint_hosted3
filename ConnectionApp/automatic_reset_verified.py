from .models import FamilyIdentity
from datetime import date, datetime


def auto_reset():

    today = datetime.today()
    # weekday = today.weekday()
    # hours = today.hour
    # minutes = today.min

    if (today.weekday() == 2) and (today.hour >= 20 and today.minute >= 57):
        families = FamilyIdentity.objects.all()
        for family in families:
            family.verified = False
            family.save()
# day -1 and time after 12 +1
