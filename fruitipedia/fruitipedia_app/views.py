from django.shortcuts import render, redirect

from fruitipedia.fruitipedia_app.models import Profile, Fruit
from fruitipedia.fruitipedia_app.forms import ProfileForm, FruitForm, FruitDeleteForm, ProfileDeleteForm


def index(request):
    """View function for the home page"""
    profile = Profile.objects.first()

    if profile:
        hide_nav = False
    else:
        hide_nav = True

    context = {
        'hide_nav': hide_nav,
    }
    return render(request, 'index.html', context)


def dashboard(request):
    """View function for the dashboard page"""
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context)


def create_fruit(request):
    """View function for the create fruit page"""
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitForm()

    context = {
        'form': form,
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    """View function for the fruit details page"""
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit,
    }
    return render(request, 'details-fruit.html', context)


def edit_fruit(request, pk):
    """View function for the fruit edit page"""
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = FruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, pk):
    """View function for the fruit delete page"""
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    else:
        form = FruitDeleteForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'delete-fruit.html', context)


def create_profile(request):
    """View function for the create profile page"""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    """View function for the profile details page"""
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {
        'profile': profile,
        'fruits_count': fruits.count(),
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    """View function for the profile edit page"""
    return render(request, 'edit-profile.html')


def delete_profile(request):
    """View function for the profile delete page"""
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'delete-profile.html')
