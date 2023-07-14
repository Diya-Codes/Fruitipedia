from django.contrib import admin
from fruitipedia.fruitipedia_app.models import Profile, Fruit


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass
