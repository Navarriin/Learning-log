from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """cadastra um usuario novo"""
    if not request.method == 'POST':
        # exibe o formulario de cadastro em branco
        form = UserCreationForm()
    else:
        # processa o formulario preenchido
        form = UserCreationForm(data=request.POST)
    
    if form.is_valid():
        # valida o formulario
        new_user = form.save()
        # faz o login do usuario e o redireciona para a home
        login(request, new_user)
        return redirect('learning_logs:index')
    
    # exibe o formulario em branco ou invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)