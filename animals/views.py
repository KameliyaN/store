from django.http import HttpResponse
from django.shortcuts import render
from animals.models import Animal
from django.core.serializers import serialize


# Create your views here.

# http://127.0.0.1:8000/animals/create/?name=%22proba%22&age=12&breed=%27somebreed&description=%27some%27&kind=%27C&image_url=https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRER2T5JEja6aPPbA6M26FO9GaHBNT4fdTMdQ&usqp=CAU
def create_animal(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    kind = request.GET.get('kind')
    breed = request.GET.get('breed')
    description = request.GET.get('description')
    image_url = request.GET.get('image_url')
    animal = Animal(name=name, age=age, kind=kind, breed=breed, description=description, image_url=image_url)
    animal.save()
    return HttpResponse('created')


def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    name = request.GET.get('name')
    animal.name = name
    return HttpResponse('edited')


def delete_animal(request, animal_id):
    Animal.objects.get(pk=animal_id).delete()
    return HttpResponse('deleted')


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
