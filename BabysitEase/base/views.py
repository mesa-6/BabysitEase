from django.shortcuts import render, redirect
from .models import Babysitter, Favorite, CustomUser, Parent
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
import string, secrets
from django.contrib import messages

CustomUser = get_user_model()

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
    if(range and intervalo):
        Babysitter_list = Babysitter.objects.filter(
            hourly_price__gte=min, 
            hourly_price__lte=max,
            experience_years__gte=inicio,
            experience_years__lte=fim
        ).select_related('user')
    elif(intervalo):
        Babysitter_list = Babysitter.objects.filter(
            experience_years__gte=inicio,
            experience_years__lte=fim
        ).select_related('user')
    elif(range):
        Babysitter_list = Babysitter.objects.filter(
            hourly_price__gte=min, 
            hourly_price__lte=max
        ).select_related('user')
    else:
        Babysitter_list=Babysitter.objects.all().select_related('user')
    # Itera sobre todas as babás cadastradas
    for babysitter_obj in Babysitter_list:
        
        # Verifica se a babá está nos favoritos do usuário
        is_favorited = favorites.filter(babysitter=babysitter_obj, user_id = user.id).exists()
        
        # Monta o payload de dados da babá para a home
        babysitter_data = {
            'name': babysitter_obj.user,
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciais inválidas.')
        else:
            messages.error(request, 'Credenciais inválidas.')
            # Aqui você pode adicionar um contador de tentativas de login e bloquear temporariamente o usuário se exceder um limite

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        last_name = request.POST['last_name']
        cpf = request.POST['cpf']
        birth_date = request.POST['birth_date']
        street = request.POST['street']
        number = request.POST['number']
        neighborhood = request.POST['neighborhood']
        zip_code = request.POST['zip_code']

        user = CustomUser(
            username=f'{name.lower()}',
            email=email,
            first_name=name,
            last_name=last_name,
            cpf=cpf,
            birth_date=birth_date,
            street=street,
            number=number,
            neighborhood=neighborhood,
            zip_code=zip_code
        )
    
        user.set_password(password)
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
            favorited = Favorite.objects.get(user_id=user.id, babysitter=post_id) 
            Favorite.delete(favorited)
        except:
            Favorite.objects.create(user_id=user, babysitter=babysitter)
    
    
    return redirect('home')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.get(email=email)

        # Gerar nova senha
        nova_senha = generate_secure_password()

        # Atualizar a senha do usuário
        user.set_password(nova_senha)

        # Salvar a nova senha
        user.save()

        # Enviar a nova senha por email
        send_mail(
            'Recuperação de senha',
            f'Sua senha é {nova_senha}',
            'gheyson.melo@ufpe.br',
            [email],
            fail_silently=False,
        )
        return redirect('login')
    return render(request, 'forgot-password.html')

class BabysitterDetailView(DetailView):
    template_name = 'babysitterDetails.html'
    queryset = Babysitter.objects.all()

class PerfilUpdate(UpdateView):
    model = Parent
    fields = ['name', 'last_name', 'street', 'number', 'neiborhood', 'zip_code', 'sex']
    template_name='form.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Parent, user_id=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["tituilo"] = "Editando Perfil"
        context["botao"] = "Atualizar"

        return context
    
def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for i in range(length))
    return secure_password
