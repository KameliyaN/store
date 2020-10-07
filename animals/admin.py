from django.contrib import admin

# Register your models here.
from animals.models import Animal #Owner

admin.site.register(Animal)
#admin.site.register(Owner)
