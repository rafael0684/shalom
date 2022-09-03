from cmd import PROMPT
import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas nao sao iguais')
            return redirect('index')
        if User.objects.filter(email = email).exists():
            print('Usuario ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('index')
        
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        nome =request.POST['email']
        senha = request.POST['password']
        
        if nome.strip() == '' or senha.strip() == '':
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('login')
        else:
            print(nome, senha)
            if User.objects.filter(email=nome).exists():
                nome = User.objects.filter(email=nome).values_list('username', flat=True).get
                print(nome)
                
            return redirect('dashboard')
        
    return render(request,'index.html')
    


def logout(request):
    return render(request, 'logout.html')

def dashboard(request):
    return render(request, 'dashboard.html')