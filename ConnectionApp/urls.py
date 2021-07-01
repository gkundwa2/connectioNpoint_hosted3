from ConnectionApp.models import FamilyIdentity
from django.urls import path
from ConnectionApp import views
# from django_filters.views import FilterView
# from ConnectionApp.models import FamilyIndentity


urlpatterns = [
    # path('', views.listpage, name='listpage'),
    path('homepage', views.homepage, name='homepage'),
    path('register/family/', views.registerpage, name='registerpage'),
    path('update/family/identity/<int:id>/', views.updatepage, name='updatepage'),
    path('listpage', views.listpage, name='listpage'),
    path('family/<int:id>/details/', views.list_details, name="list_details"),
    path('unverify-verify/<int:pk>', views.verify, name="verify"),
    path('record/new/transaction/for/<str:fname>/<str:lname>/family/<int:id>/', views.create_transaction, name="new_transaction"),
    path("transactions/list/", views.transactions_list, name="transactions_list"),

    path("delete/transaction/<int:id>/warning/", views.delete_warning_trans, name="delete_warning_trans"),
    path("delete/transaction/<int:id>/", views.delete_transaction, name="delete_transaction"),
    path("delete/family/identity/<int:id>/", views.delete_family, name="delete_family"),
    path("delete/family/identity/<int:id>/warning/", views.delete_warning_family, name="delete_warning_family"),




]
