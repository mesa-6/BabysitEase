from django.contrib import admin
from .models import Babysitter, Parent, Favorite, CustomUser, Schedule, Message, Feedback, BabysitterRating

class BabysitterRatingInline(admin.TabularInline):
    model = BabysitterRating

class BabysitterAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'rating_average')
    inlines = [BabysitterRatingInline]

admin.site.register(Babysitter, BabysitterAdmin)
admin.site.register(Parent)
admin.site.register(Favorite)
admin.site.register(CustomUser)
admin.site.register(Schedule)
admin.site.register(Message)
admin.site.register(Feedback)
admin.site.register(BabysitterRating)