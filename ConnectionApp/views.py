from django.shortcuts import render, redirect
from django.http import HttpResponse
from ConnectionApp.models import FamilyIdentity
from ConnectionApp.forms import DatabaseForm
from django.contrib import messages
from .filters import FamilyFilter

from django.core.paginator import Paginator


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
    search_option = ""
    search_pattern = ""
    if request.GET.get("search_option", False):
        search_option = request.GET.get("search_option")
        search_pattern = request.GET.get("search_pattern")

        if search_option.strip().lower() == "first_name":
            all_families = FamilyIdentity.objects.filter(firstName__icontains=search_pattern)
        elif search_option.strip().lower() == "last_name":
            all_families = FamilyIdentity.objects.filter(lastName__icontains=search_pattern)
        elif search_option.strip().lower() == "family_members":
            all_families = FamilyIdentity.objects.filter(familyMembers__icontains=search_pattern)


    paginator = Paginator(all_families, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj,
                'search_option': search_option,
                'search_pattern': search_pattern}
    return render(request, 'listpage.html', context)

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
