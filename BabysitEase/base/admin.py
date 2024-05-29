from django.contrib import admin
from .models import Babysitter, Parent, Favorite, CustomUser, Schedule, Converstions, Message

# Register your models here.
admin.site.register(Babysitter)
admin.site.register(Parent)
admin.site.register(Favorite)
admin.site.register(CustomUser)
admin.site.register(Schedule)
admin.site.register(Converstions)
admin.site.register(Message)
