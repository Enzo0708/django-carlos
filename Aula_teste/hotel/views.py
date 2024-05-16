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

            user = usuario(nome=var_nome, email=var_email)
            user.save()

            return HttpResponse("<h1>thanks</h1>")   
    else:
        form = FormNome()
    return render(request, "nome.html", {"form": form})