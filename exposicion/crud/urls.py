from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', view=views.home, name='homePage' ),
    path('update/<int:id>', view=views.update, name='updatePelicula'),
    path('delete/<int:id>', view=views.delete, name='deletePelicula'),
    path('', view=views.homeRedictect, name='redirecToHome')
]
