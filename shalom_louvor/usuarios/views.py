from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from louvor.models import Musica, Artista


def login(request):
    if request.method == 'POST':
        email =request.POST['email']
        senha = request.POST['senha']
        
        if email.strip() == '' or senha.strip() == '':
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('musica')
        else:
            print(email, senha)
            if User.objects.filter(email=email).exists():
                
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print('Login realizado com sucesso')   
                    return redirect('dashboard')
                else:
                    print('deu ruim o user eh None')
            else:
                print('email nao existe usuario com esse email')
        return render(request,'musica.html')
    
    

def cadastro(request):
    if request.method == 'POST':
        
        nome = request.POST['nome'].capitalize()
        sobrenome = request.POST['sobrenome'].capitalize()
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        username= nome.lower()+sobrenome.lower()

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('index')
        if senha != senha2:
            print('As senhas nao sao iguais')
            return redirect('index')
        if User.objects.filter(email = email).exists():
            print('Usuario ja cadastrado')
            return redirect('index')
        user = User.objects.create_user(username=username, first_name=nome, last_name=sobrenome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        user = auth.authenticate(request, username=username, password=senha)
        auth.login(request, user)
        return redirect('dashboard')
        
    else:
        return render(request, 'cadastro.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    musicas = Musica.objects.order_by('-data_musica').all
    dados = {
        'musicas' : musicas
    }
    return render(request, 'dashboard.html', dados)