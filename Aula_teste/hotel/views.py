from django.shortcuts import render, HttpResponse
from .models import hotel, quarto

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)