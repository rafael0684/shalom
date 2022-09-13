from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages



def login(request):
    '''Realiza o login de usuarios'''
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
    """Realiza cadastro de novo usuario"""
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
    '''Realiza o logout do usuario'''
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('index')

