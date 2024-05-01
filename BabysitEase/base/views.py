from django.shortcuts import render, redirect
from .models import Babysitter, Favorite, CustomUser
from django.views.generic import DetailView
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    # Recebe o usuário logado
    user = request.user
    range=request.GET.get("range")
    intervalo=request.GET.get("intervalo")
    if(range):
        min, max=range.split(',')
    if(intervalo):
        inicio, fim=intervalo.split(',')
    
    
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user_id=user.id)
    
    # Inicializa o array de babás que vai para a home
    babysitters = []
    if(range):
        Babysitter_list = Babysitter.objects.filter(hourly_price__gte=min, hourly_price__lte=max)
    elif(intervalo):
        Babysitter_list = Babysitter.objects.filter(experience_years__gte=inicio,experience_years__lte=fim)
    elif(range and intervalo):
        Babysitter_list = Babysitter.objects.filter(hourly_price__gte=min, hourly_price__lte=max,experience_years__gte=inicio,experience_years__lte=fim)
    else:
        Babysitter_list=Babysitter.objects.all()
    # Itera sobre todas as babás cadastradas
    for babysitter_obj in Babysitter_list:
        
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
    from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # se entrou aqui, é porque as credenciais estão corretas e o usuário foi autenticado
            return redirect('home')
        else:
            # se entrou aqui, é porque as credenciais estão erradas
            print('Credenciais inválidas. Por favor, tente novamente.')
            return render(request, 'login.html', {'error_message': 'Credenciais inválidas. Por favor, tente novamente.'})
    else:
        # se entrou aqui, é porque o método não foi POST
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        last_name = request.POST['last_name']
        cpf = request.POST['cpf']
        birth_date = request.POST['birth_date']
        sex = request.POST['sex']
        street = request.POST['street']
        number = request.POST['number']
        neighborhood = request.POST['neighborhood']
        zip_code = request.POST['zip_code']

        user = CustomUser.objects.create_user(
            username=f'{name} {last_name}',
            email=email,
            password=password,
            name=name,
            last_name=last_name,
            cpf=cpf,
            birth_date=birth_date,
            sex=sex,
            street=street,
            number=number,
            neighborhood=neighborhood,
            zip_code=zip_code
        )

        user.save()
        
        return redirect('login')
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