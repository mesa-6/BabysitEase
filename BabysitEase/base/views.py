from django.contrib.auth import authenticate, login, get_user_model
from .models import Babysitter, Favorite, CustomUser, Feedback, Schedule,Message
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
import string, secrets
import json

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

def favorited_babyssiter(request, pk):
    user = request.user

    if request.method == 'POST':
        babysitter = Babysitter.objects.get(cpf=pk)
        
        favorited = {}
        
        try:
            favorited = Favorite.objects.get(user=user, babysitter=pk) 
            Favorite.delete(favorited)
        except:
            Favorite.objects.create(user=user, babysitter=babysitter)
    
    
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
            f'Recuperação de senha',
            f'Olá {user.get_username().capitalize()}, você está recebendo esse email pois houve uma solicitação de recuperação de senha no BabysitEase. Então, sua nova senha é {nova_senha}. Por favor, altere sua senha assim que possível na aba editar perfil.',
            'gheyson.melo@ufpe.br',
            [email],
            fail_silently=False,
        )
        return redirect('login')
    return render(request, 'forgot-password.html')

def schedules_solicitation(request):
    if request.method == 'POST':
       
        # Supondo que 'data' contenha os bytes recebidos
        data_bytes = request.body

        # Decodificar os bytes para uma string
        data_string = data_bytes.decode('utf-8')

        # Analisar o JSON
        parsed_data = json.loads(data_string)

        # Acessar o array de objetos 'schedules'
        schedules = parsed_data['schedules']

        # Agora você pode trabalhar com o array 'schedules' conforme necessário
        for schedule in schedules:
            # Transformando o 'id' em um inteiro
            id = int(schedule['id'])

            # Buscando o Schedule pelo id
            schedule_obj = Schedule.objects.get(id=id)

            # Atualizando o status do Schedule
            schedule_obj.status = 'Pendente'

            # Salvando o Schedule
            schedule_obj.save()

        # Retorna uma resposta de sucesso
        return JsonResponse({'message': 'Solicitação enviada com sucesso'}, status=200)

    # Se o método da solicitação não for POST, retorne um erro
    return JsonResponse({'error': 'Método não permitido'}, status=405)

class BabysitterDetailView(DetailView):
    template_name = 'babysitterDetails.html'
    queryset = Babysitter.objects.all()

class BabysitterDetailView(DetailView):
    template_name = 'babysitterDetails.html'
    model = Babysitter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        babysitter = self.get_object() 

        # Adiciona o objeto Babysitter ao contexto
        context['babysitter'] = babysitter

        # Obtém todos os horários relacionados a esta babá
        schedules = Schedule.objects.filter(babysitter=babysitter)

        schedule_info = []

        for schedule in schedules:
            schedule = str(schedule)
            # Divida a string por "-" para extrair informações
            schedule_parts = schedule.split('-')

            # Extrair o dia, o período do dia e o status de disponibilidade
            day = schedule_parts[1]
            time_of_day = schedule_parts[2]
            availability = schedule_parts[3]
            id = schedule_parts[4]

            # Adicione as informações extraídas ao array
            schedule_info.append({
                'id': id,
                'day': day,
                'period': time_of_day,
                'status': availability
            })
            
        # Dicionário para mapear os dias da semana para números
        day_order = {
            'monday': 1,
            'tuesday': 2,
            'wednesday': 3,
            'thursday': 4,
            'friday': 5,
            'saturday': 6,
            'sunday': 7
        }

        period_order = {
            'morning': 1,
            'afternoon': 2,
            'night': 3
        }

        # Ordena os horários por dia e período do dia
        schedule_info.sort(key=lambda x: (day_order[x['day']], period_order[x['period']]))

        # Busca os feedbacks da babá
        feedbacks = Feedback.objects.filter(babysitter=babysitter)

        feedbacks_array = []

        for feedback in feedbacks:
            # Transforme o feedback em uma string
            feedback = str(feedback)

            # Divide a string por "-" para extrair informações
            feedback_parts = feedback.split('-')

            # Extrai o usuário, o feedback e a data de criação
            user = feedback_parts[1]
            feedback = feedback_parts[2]
            created_at = feedback_parts[3]

            # Adiciona as informações ao array
            feedbacks_array.append({
                'user': user,
                'feedback': feedback,
                'created_at': created_at
            })

        # Adiciona os horários ao contexto
        context['schedules'] = schedule_info

        # Adiciona os feedbacks ao contexto
        context['feedbacks'] = feedbacks_array

        return context

class PerfilUpdate(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'street', 'number', 'neighborhood', 'zip_code', 'sex']
    template_name = 'form.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editando Perfil"
        context["botao"] = "Atualizar"
        return context

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for i in range(length))
    return secure_password

def show_messages(request):
    babysitter_list = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            babysitter_cpf = request.POST.get('cpf')

            print(request)
            print(babysitter_cpf)

            babysitter = Babysitter.objects.get(cpf=babysitter_cpf)
            text = request.POST['text']
            Message.objects.create(user=user, Babysitter=babysitter, message=text)
            

    messages = Message.objects.all()
    
    return render(request, "messages.html", {"messages": messages})
