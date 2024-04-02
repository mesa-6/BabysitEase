from django.shortcuts import render
from .models import baba


# Create your views here.
def home(request):
    babas = baba.objects.all()
    context = {'babas': babas}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')