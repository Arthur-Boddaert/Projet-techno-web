from django.shortcuts import render

def index(request):
    return render(request, 'accueil.html')

def guide(request):
    return render(request, 'guide.html')

def enonce(request):
    return render(request, template_name='enonce-projet2-2022.html')