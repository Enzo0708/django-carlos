from django import forms

class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    sobre_nome = forms.CharField(label='Sobrenome', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    idade = forms.IntegerField(label='Idade')
    endereco = forms.CharField(label='Endereço', max_length=50)
    quarto = [
        ('solteiro', 'Quarto Solteiro'),
        ('casal', 'Quarto Casal'),
        ('conforto', 'Quarto Conforto'),
        ('luxo', 'Quarto Luxo')
    ]
    quarto_de_escolha = forms.ChoiceField(choices=quarto, label='Quarto de escolha')
    data = forms.DateField(label='Data da Reserva', widget=forms.SelectDateWidget)