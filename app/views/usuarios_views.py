from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuarios(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('logar_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuarios.html',{"form_usuario":form_usuario})


def logar_usuario(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request,username=username,
                               password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'Suas credenciais não funcionaram, verifique seu usuario e senha')
            return redirect('logar_usuario')
    else:
       form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html',{"form_login":form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')
