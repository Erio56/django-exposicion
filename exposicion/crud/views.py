from django.shortcuts import render, redirect
from .models import Pelicula

from .forms import peliculaForm

# Create your views here.

def home(request):
   
   
   #Forms o a mano
   if request.method == 'POST':
      pelicula = peliculaForm(request.POST)
      pelicula.save()
      return redirect('/home/')
      
   if request.method == 'GET':
      formulario = peliculaForm()
      peliculas = Pelicula.objects.all().order_by('-id')
      context = {'peliculas': peliculas,
                'formulario': formulario}
      
      return render(request,'home.html', context=context)
   
   
   return render(request,'home.html')

def update(request, id):
   if request.method == 'GET':
      form = peliculaForm(instance=Pelicula.objects.get(id=id))

      context = {
         'formulario': form,
         'id': id
      }
      
      return render(request, 'update.html', context=context)
   
   if request.method == 'POST':
      pelicula = peliculaForm(request.POST)
      pelicula.save()
      return redirect('/home/')




def delete(request, id):
   pelicula = Pelicula.objects.get(id=id)
   pelicula.delete()

   return redirect('/home/')

def homeRedictect(request):
   return redirect('/home/')