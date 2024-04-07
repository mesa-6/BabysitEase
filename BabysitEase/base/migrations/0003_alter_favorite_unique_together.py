# Generated by Django 5.0.3 on 2024-04-07 14:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_parent_favorited_babysitter_favorited'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('babysitter_cpf', 'user_id')},
        ),
    ]
