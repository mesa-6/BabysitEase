from django.shortcuts import render, redirect
from .models import Babysitter, Favorite
from django.views.generic import DetailView

# Create your views here.
def home(request):

    # Recebe o usuário logado
    user = request.user
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user_id=user.id)
    
    # Inicializa o array de babás que vai para a home
    babysitters = []
    
    # Itera sobre todas as babás cadastradas
    for babysitter_obj in Babysitter.objects.all():
        
        # Verifica se a babá está nos favoritos do usuário
        is_favorited = favorites.filter(babysitter_cpf=babysitter_obj.cpf, user_id = user.id).exists()
        
        # Monta o payload de dados da babá para a home
        babysitter_data = {
            'name': babysitter_obj.name,
            'description': babysitter_obj.description,
            'hourly_price': babysitter_obj.hourly_price,
            'favorited': is_favorited,  
            'cpf': babysitter_obj.cpf,
        }
        
        # Adiciona a babá ao array de babás
        babysitters.append(babysitter_data)
    
    # Ordena as babás pelo atributo favorited
    babysitters.sort(key=lambda x: x['favorited'], reverse=True)
        
    # Monta o contexto da home
    context = {
        'babysitters': babysitters,  
        'user': user
    }
    
    # Renderiza a home
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')

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

class BabysitterDetailView(DetailView):
    template_name = 'babysitterDetails.html'
    queryset = Babysitter.objects.all()