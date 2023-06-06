from django.shortcuts import render

# Create your views here.

def signup (request): 
    return render(request, 'signup.html')

def home(request):
    if request.method == 'POST':

        return render(request, 'success.html')
    return render(request, 'home.html')


def vehicles(request):
    return render(request, 'vehicles.html')

def electronics(request):
    return render(request, 'electronics.html')

def sports(request):
    return render(request, 'sports.html')
