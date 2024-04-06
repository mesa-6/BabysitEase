from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # profile_pic = models.ImageField()

    def __str__(self):
        return self.cpf

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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    favorited = models.ManyToManyField(Babysitter, default=None, blank=True, related_name='favorited')
    # profile_pic = models.ImageField()

    def __str__(self):
        return self.cpf
    
    @property
    def num_likes(self):
        return self.favorited.all().count()


class Favorite(models.Model):
    babysitter_cpf = models.ForeignKey(Babysitter, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)

    def __str__(self):
        return {self.babysitter_cpf, self.user_id, self.value}