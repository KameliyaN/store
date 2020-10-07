from django.http import HttpResponse
from django.shortcuts import render
from .models import Animal
from django.core.serializers import serialize


# Create your views here.
def serialized_data(data):
    try:
        return serialize('json', data)
    except Exception as exe:
        return serialize('json', [data])


def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return serialized_data(animal)
    animals = Animal.objects.all()

    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(request):
    dogs = Animal.objects.filter(kind='D')
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by('age')
    return HttpResponse(serialized_data(animals))


def get_all_cats(request):
    cats = Animal.objects.filter(kind='C')
    return HttpResponse(serialized_data(cats))
