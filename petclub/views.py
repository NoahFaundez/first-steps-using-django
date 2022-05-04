from django.shortcuts import render

# Create your views here.

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello World with DRF!", status=200) # respuesta del servicio

class PetClubView(APIView):
    def get(self, request):
        pets = {
            "id": 1,
            "species": "Pug",
            "name": "Firulais",
            "age": 7,
            "color": "Cafe",
        }
        return Response(data=pets, status=200)
    
    def post(self, request):
        return Response(data="POST", status=200)

    def patch(self, request):
        return Response(data="PATCH", status=200)

    def delete(self, request):
        return Response(data="DELETE", status=200)

class PersonClubView(APIView):
    def get(self, request):
        person = {
            "id": 1,
            "email": "correoFalso123@xd.com",
            "first_name": "Juan",
            "last_name": "Perez",
            "rut": "123334445",
        }
        return Response(data=person, status=200)
    
    def post(self, request):
        return Response(data="POST", status=200)

    def patch(self, request):
        return Response(data="PATCH", status=200)

    def delete(self, request):
        return Response(data="DELETE", status=200)