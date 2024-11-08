from django.shortcuts import render,redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form =LoginForm(request.POST)

        if form.is_valid():
            nome=form["login"].value()
            senha=form["senha"].value()

            usuario= auth.authenticate(request,username=nome,password=senha,
                          )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso")
                return redirect('index')
            else:
                messages.error(request,"Login ou senha incorretos")
                return redirect('login')


    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            
            
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,"Já existe um usuário com esse nome")
                return redirect('cadastro')
            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
            messages.success(request, f"{nome} cadastrado com sucesso")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"forms": form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Você foi deslogado com sucesso!")
        return redirect('login')
    else:
        messages.error(request, "Você não está logado!")
        return redirect('cadastro')