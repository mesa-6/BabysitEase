from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    name= models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, blank=True)

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='customuser_set')

    class Meta:
        permissions = [
            ('can_view_customuser', _('Can view custom users')),
        ]

class Babysitter(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    hourly_price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField()
    experience_years = models.IntegerField()
    documents_submitted = models.BooleanField()
    education_level = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=80)
    neiborhood = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    description = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorited = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='favorited')

    def __str__(self):
        return self.cpf
    
    @property
    def num_likes(self):
        return self.favorited.all().count()

class Parent(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    neiborhood = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf


class Favorite(models.Model):
    babysitter_cpf = models.ForeignKey(Babysitter, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)

    class Meta:
        unique_together = ('babysitter_cpf', 'user_id')

    def str(self):
        return f'{self.babysitter_cpf} - {self.user_id}'
    
    