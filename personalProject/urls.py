"""personalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (path, include)

from petclub.views import (
    HelloWorld, 
    PetClubView, 
    PersonClubView
)

urlpatterns = [
    path('hi', HelloWorld.as_view(), name="helloworld"),
    path('pets', PetClubView.as_view(), name="get"),
    path('patchPets', PetClubView.as_view(), name="patch"),
    path('postPets', PetClubView.as_view(), name="post"),
    path('deletePets', PetClubView.as_view(), name="delete"),
    path('person', PersonClubView.as_view(), name="get"),
    path('patchPerson', PersonClubView.as_view(), name="patch"),
    path('postPerson', PersonClubView.as_view(), name="post"),
    path('deletePerson', PersonClubView.as_view(), name="delete"),
    path('api-auth/', include('rest_framework.urls'))
]
