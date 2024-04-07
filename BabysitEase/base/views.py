from django.shortcuts import render, redirect
from .models import Babysitter, Favorite

# Create your views here.
def home(request):
    user = request.user
    
    favorites = Favorite.objects.filter(user_id=user.id)
    
    babysitters = []
    
    for babysitter_obj in Babysitter.objects.all():
        
        is_favorited = favorites.filter(babysitter_cpf=babysitter_obj.cpf, user_id = user.id).exists()
        
        
        babysitter_data = {
            'name': babysitter_obj.name,
            'description': babysitter_obj.description,
            'hourly_price': babysitter_obj.hourly_price,
            'favorited': is_favorited,  
            'cpf': babysitter_obj.cpf,
        }
        
        
        babysitters.append(babysitter_data)
        
    
        
    
    context = {
        'qs': babysitters,  
        'user': user,
        'favorites': favorites,
    }
    
    return render(request, 'home.html', context)



def room(request):
    return render(request, 'room.html')


def favorited_babyssiter(request):
    user = request.user
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        babysitter = Babysitter.objects.get(cpf=post_id)
        
        favorited = {}
        
        try:
            favorited = Favorite.objects.get(user_id=user.id, babysitter_cpf=post_id) 
            Favorite.delete(favorited)
        except:
            Favorite.objects.create(user_id=user, babysitter_cpf=babysitter)
    
    
    return redirect('home')