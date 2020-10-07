from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('^all/$', views.get_all_animals, name='all'),
    path('all/<int:animal_id>/', views.get_animal, name='animal'),
    path('all/dogs/', views.get_all_dogs, name='dogs'),
    path('all/ordered/', views.order_animals, name='all_ordered'),
    path('all/cats/', views.get_all_cats, name='cats')
]
