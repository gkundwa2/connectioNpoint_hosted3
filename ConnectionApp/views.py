from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from ConnectionApp.models import *
from django.contrib.auth.decorators import login_required
from .automatic_reset_verified import auto_reset


# Homepage / Search
@login_required
def homepage(request):
    auto_reset()
    return render(request, 'homepage.html', {})

# List page function


@login_required
def listpage(request):

    auto_reset()
    all_families = FamilyIdentity.objects.all()
    search_option = ""
    search_pattern = ""
    if request.GET.get("search_option", False):
        search_option = request.GET.get("search_option")
        search_pattern = request.GET.get("search_pattern")

        if search_option.strip().lower() == "first_name":
            all_families = FamilyIdentity.objects.filter(
                firstName__icontains=search_pattern)
        elif search_option.strip().lower() == "last_name":
            all_families = FamilyIdentity.objects.filter(
                lastName__icontains=search_pattern)
        elif search_option.strip().lower() == "family_members":
            all_families = FamilyIdentity.objects.filter(
                familyMembers__icontains=search_pattern)
        elif search_option.strip().lower() == "phone":
            all_families = FamilyIdentity.objects.filter(
                phone__icontains=search_pattern)

    paginator = Paginator(all_families, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj,
               'search_option': search_option,
               'search_pattern': search_pattern}
    return render(request, 'listpage.html', context)

# register page function


@login_required
def list_details(request, id):
    auto_reset()
    page_obj = []
    family = {}
    from_date = ""
    to_date = ""
    try:
        family = FamilyIdentity.objects.get(id=id)
        transactions = Transaction.objects.filter(
            family=family).order_by("-trans_date")

        if request.GET.get("from_date", None):
            from_date = request.GET.get("from_date")
            to_date = request.GET.get("to_date")
            transactions = Transaction.objects.filter(
                family=family, trans_date__gte=from_date, trans_date__lte=to_date).order_by("-trans_date")

        paginator = Paginator(transactions, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        pass
    return render(request, "family_details.html",
                  {"fam": family, "page_obj": page_obj, "from_date": from_date,
                   "to_date": to_date})


@login_required
def registerpage(request):
    auto_reset()
    if request.method == "POST":
        firstName = request.POST.get('firstName', "-")
        lastName = request.POST.get('lastName', "-")
        middleName = request.POST.get('middleName', "-")
        familyMembers = request.POST.get('familyMembers', 0)
        phone = request.POST.get("phone", "-")
        document = request.POST.get("official_doc", "-")

        family_identity = FamilyIdentity(
            firstName=firstName,
            lastName=lastName,
            middleName=middleName,
            familyMembers=familyMembers,
            phone=phone,
            # national_doc=document
        )
        family_identity.save()
        messages.success(
            request, ("New Family has been registered successfully!"))
        return redirect('listpage')

    return render(request, 'registerpage.html', {})


@login_required
def updatepage(request, id):
    auto_reset()
    fam = None
    if request.method == "POST":
        firstName = request.POST.get('firstName', "-")
        lastName = request.POST.get('lastName', "-")
        middleName = request.POST.get('middleName', "-")
        familyMembers = request.POST.get('familyMembers', 0)
        phone = request.POST.get("phone", "-")
        document = request.POST.get("official_doc", "-")
        try:
            family_identity = FamilyIdentity.objects.get(pk=id)
            family_identity.firstName = firstName
            family_identity.lastName = lastName
            family_identity.middleName = middleName
            family_identity.familyMembers = familyMembers
            family_identity.phone = phone

            family_identity.save()
            messages.success(
                request, ("Family identification has been updated successfully!"))
            return redirect('listpage')
        except Exception as e:
            pass
    try:
        fam = FamilyIdentity.objects.get(pk=id)
    except Exception as e:
        pass
    return render(request, 'registerpage.html', {"fam": fam})


@login_required
def verify(request, pk):
    auto_reset()
    try:
        family_identity = FamilyIdentity.objects.get(id=pk)
        family_identity.setVerified()
        return redirect('listpage')
    except FamilyIdentity.DOESNOTEXIST:
        return redirect('listpage')


@login_required
def delete_warning_family(request, id):
    auto_reset()
    fam = None
    try:
        fam = FamilyIdentity.objects.get(pk=id)
    except Exception as e:
        pass
    return render(request, "delete_page_warning.html", {"fam": fam})


def delete_family(request, id):
    auto_reset()
    try:
        fam = FamilyIdentity.objects.get(pk=id)
        fam.delete()
    except Exception as e:
        pass
    return redirect("listpage")


################# views functions for transactions #####################
@login_required
def create_transaction(request, fname, lname, id):
    auto_reset()
    if request.method == "POST":
        try:
            family_identity = FamilyIdentity.objects.get(pk=id)
            note = request.POST.get("note", "-")
            trans = Transaction(family=family_identity, food_given=note)
            trans.save()
            messages.success(
                request, "New Family Transaction Recorded Successfully!")
        except Exception as e:
            pass
    return redirect("list_details", id)


@login_required
def delete_warning_trans(request, id):
    auto_reset()
    trans = None
    try:
        trans = Transaction.objects.get(pk=id)
    except Exception as e:
        pass
    print("Trans: ", trans)
    return render(request, "delete_warning_trans.html", {"trans": trans})


@login_required
def delete_transaction(request, id):
    auto_reset()
    new_id = 0
    try:
        trans = Transaction.objects.get(pk=id)
        new_id = trans.family.id
        trans.delete()
        return redirect("list_details", new_id)
    except Exception as e:
        pass
    return redirect("listpage")


@login_required
def transactions_list(request):
    auto_reset()
    famillies = []
    members = 0
    from_date = ""
    to_date = ""

    transactions = Transaction.objects.all().order_by("-trans_date")

    if request.GET.get("from_date", None):
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        transactions = Transaction.objects.filter(
            trans_date__gte=from_date, trans_date__lte=to_date).order_by("-trans_date")

    paginator = Paginator(transactions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for trans in transactions:
        if trans.family not in famillies:
            famillies.append(trans.family)
    for fam in famillies:
        members += fam.familyMembers
    context = {"famillies": len(famillies),
               "members": members,
               "page_obj": page_obj,
               "from_date": from_date,
               "to_date": to_date}
    return render(request, "transactions_list.html", context)
