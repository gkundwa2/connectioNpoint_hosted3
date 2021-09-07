
from django.contrib import admin
from django.urls import path, include
from ConnectionApp import views

urlpatterns = [
    path('pastor/admin/', admin.site.urls),
    path('connectionpantry/', include('ConnectionApp.urls')),
    path('account/', include('users_app.urls')),
    path("", views.homepage),

]
