from django.shortcuts import render
from .models import Babysitter
# Create your views here.
def home(request):
    # chamando os dados das babas do banco de dados
    babysitters=Babysitter.objects.all()
    context_babysitters={
        'babysitters':babysitters
    }
    
    return render(request, 'home.html', context_babysitters) 

def room(request):
    return render(request, 'room.html')