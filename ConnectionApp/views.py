from django.shortcuts import render, redirect
from django.http import HttpResponse
from ConnectionApp.models import FamilyIdentity
from ConnectionApp.forms import DatabaseForm
from django.contrib import messages
from .filters import FamilyFilter


# Homepage / Search
def homepage(request):
    context = {}
    all_families = FamilyIdentity.objects.all()
    filtered_person = FamilyFilter(
        request.GET,
        queryset=all_families
    )
    context['filtered_person'] = filtered_person.qs
    return render(request, 'homepage.html', context=context)

# List page function


def listpage(request):
    all_families = FamilyIdentity.objects.all()
    return render(request, 'listpage.html', {'all_families': all_families})

# register page function


def registerpage(request):
    if request.method == "POST":
        print(f'This is the printed {request.POST}')
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        middleName = request.POST['middleName']
        familyMembers = request.POST['familyMembers']

        family_identity = FamilyIdentity(
            firstName=firstName,
            lastName=lastName,
            middleName=middleName,
            familyMembers=familyMembers
        )
        family_identity.save()
        messages.success(request, ("New Family Member added!"))
        return redirect('listpage')
    else:
        all_families = FamilyIdentity.objects.all()
        return render(request, 'registerpage.html', {'all_families': all_families})


def verify(request, pk):
    try:
        family_identity = FamilyIdentity.objects.get(id=pk)
        family_identity.setVerified()
        return redirect('listpage')
    except FamilyIdentity.DOESNOTEXIST:
        return redirect('listpage')
