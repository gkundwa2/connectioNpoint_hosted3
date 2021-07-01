
from django.contrib import admin
from django.urls import path, include
from ConnectionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connectionpantry/', include('ConnectionApp.urls')),
    path("", views.homepage),
]
