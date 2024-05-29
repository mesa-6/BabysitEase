from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    street = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, blank=True)

class Babysitter(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    hourly_price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField()
    experience_years = models.IntegerField()
    documents_submitted = models.BooleanField()
    education_level = models.CharField(max_length=50)
    description = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # favorited = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='favorited')

    def __str__(self):
        return self.cpf
    
    @property
    def num_likes(self):
        return self.favorited.all().count()

class Parent(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf

class Favorite(models.Model):
    babysitter = models.ForeignKey(Babysitter, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)

    class Meta:
        unique_together = ('babysitter', 'user')

    def __str__(self):
        return f'{self.babysitter} - {self.user}'

class Schedule(models.Model):
    babysitter = models.ForeignKey(Babysitter, on_delete=models.CASCADE)
    status=models.CharField(max_length=15,choices=[('Disponível','Disponível'),('Indisponível','Indisponível'), ('Pendente','Pendente')])
    period = models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('night', 'Night')], max_length=10)
    day = models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10)

    class Meta:
        unique_together = ('babysitter', 'day', 'period')

    def __str__(self):
        return f'{self.babysitter}-{self.day}-{self.period}-{self.status.capitalize()}-{self.id}'

class Converstions(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    title = models.CharField( max_length=200)
    messanges = models.ManyToManyField ('Message', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return {self.user.username}