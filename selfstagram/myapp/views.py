from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Image
from .forms import ImageForm

# def home(request):
#     if request.method == "POST":
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     img = Image.objects.all()
        
#     form = ImageForm()
#     return render(request, 'myapp/home.html', {"img" : img, "form" : form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect('home')
    else:
        form = ImageForm()
    
    # Get only the current user's images, ordered by date (newest first)
    images = Image.objects.filter(user=request.user).order_by('-date')
    return render(request, 'myapp/home.html', {'img': images, 'form': form})

    