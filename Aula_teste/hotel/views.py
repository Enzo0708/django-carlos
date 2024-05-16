from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, usuario
from .forms import FormNome

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def page_quartos(request):
    context = {}
    dados_quartos = quarto.objects.all()
    context["dados_quartos"] = dados_quartos
    return render(request, 'quartos.html', context)

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():

            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_sobre_nome = form.cleaned_data['sobre_nome']
            var_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']

            user = usuario(nome=var_nome, email=var_email, sobre_nome=var_sobre_nome, idade=var_idade, endereco=var_endereco, quarto=var_quarto, data=var_data)
            user.save()

            return HttpResponse("<h1>thanks</h1>")   
    else:
        form = FormNome()
    return render(request, "reserva.html", {"form": form})