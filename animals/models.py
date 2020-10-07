from django.db import models


# Create your models here.


# class Owner(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)


class Animal(models.Model):
    KIND_CHOICES = (
        ('D', 'dog'),
        ('C', 'cat')
    )
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    image_url = models.URLField()
    description = models.TextField()
    #owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.name} and i am {self.age}'
