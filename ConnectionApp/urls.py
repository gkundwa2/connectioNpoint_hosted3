from ConnectionApp.models import FamilyIdentity
from django.urls import path
from ConnectionApp import views
# from django_filters.views import FilterView
# from ConnectionApp.models import FamilyIndentity


urlpatterns = [
    # path('', views.listpage, name='listpage'),
    path('homepage', views.homepage, name='homepage'),
    path('registerpage', views.registerpage, name='registerpage'),
    path('listpage', views.listpage, name='listpage'),
    path('unverify-verify/<int:pk>', views.verify, name="verify")

]
