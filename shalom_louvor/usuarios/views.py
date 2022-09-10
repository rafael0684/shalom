from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from louvor.models import Musica, Artista


def login(request):
    if request.method == 'POST':
        email =request.POST['email']
        senha = request.POST['senha']
        
        if email.strip() == '' or senha.strip() == '':
            messages.ERROR(request, 'Os campos email e senha nao podem ficar em branco')
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('index')
        else:
            print(email, senha)
            if User.objects.filter(email=email).exists():
                
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print('Login realizado com sucesso')
                    messages.success(request, 'Login realizado com sucesso')
                    return redirect('dashboard' )
                else:
                    print('deu ruim o user eh None')
                    messages.error(request, 'Erro no login')
            else:
                messages.error(request, 'Nao existe usuario cadastrado com esse email')
                print('Nao existe usuario cadastrado com esse email')
        return render(request,'index.html')
    
    

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
            messages.error(request, 'O campo nome nao pode ficar em branco')
            return redirect('index')
        if senha != senha2:
            print('As senhas nao sao iguais')
            messages.error(request, 'As senhas nao sao iguais')
            return redirect('index')
        if User.objects.filter(email = email).exists():
            print('Usuario ja cadastrado')
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('index')
        user = User.objects.create_user(username=username, first_name=nome, last_name=sobrenome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        messages.success(request, 'Usuario cadastrado com sucesso')
        user = auth.authenticate(request, username=username, password=senha)
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso')
        return redirect('dashboard')
        
    else:
        return render(request, 'cadastro.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('index')

def dashboard(request):
    musicas = Musica.objects.order_by('-data_musica').all
    dados = {
        'musicas' : musicas
    }
    
    return render(request, 'dashboard.html', dados)

def criarMusica(request):
    artistas = Artista.objects.order_by('nome_artista')
    dados = {
        'artistas': artistas,    
    }
    

    if request.method == 'POST':
        titulo_musica = request.POST['titulo_musica'].strip()
        input_artista = request.POST['nome_artista']
        nome_artista = get_object_or_404(Artista, nome_artista=input_artista)
        release_year = request.POST['release_year']
        lyrics = request.POST['lyrics']
    
        nova_musica = Musica.objects.create(titulo_musica=titulo_musica, 
                                            nome_artista=nome_artista,
                                            release_year=release_year,
                                            lyrics=lyrics
                                            )
        nova_musica.save()
        messages.success(request, "Musica adicionada com sucesso")
        
        render(request, "criarMusica.html")
    
    return render(request, 'criarMusica.html', dados)