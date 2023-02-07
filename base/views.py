from .models import Baqueros, Caballos, FloraFauna, Post, Comment
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

#########################################################

def home(request):
    posts = Post.objects.all() #se puede ordenar, despues del "objects." colocar "order_by('X')" siendo "X" como se ordenaría. Ej: cambiando la "X" por "-created" se ordenara por fecha de más reciente a la más vieja
    return render(request, 'home.html', {'posts': posts})

def loginPage(request):
    if (request.method == "POST"):
        username= request.POST.get('username')
        password= request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Estas dentro de "El Pentágono"')
                return redirect('/')
        messages.error(request, 'Estas comprometido, sal corriendo agente "Django"')

    return render(request, 'login.html')

def registerPage(request):
    if (request.method == 'POST'):
            name= request.POST.get('name')
            last_name= request.POST.get('last_name')
            username= request.POST.get('username')
            email= request.POST.get('email')
            password= request.POST.get('password')
            confirm_password= request.POST.get('confirm_password')
            if (password != confirm_password):
                messages.error(request, 'Las contraseñas son distintas')
                return redirect ('/register')
            User.objects.create_user(username, email=email, first_name=name, last_name=last_name, password=password)
        
    return render(request, 'register.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def post(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Post.objects.create(
                title= request.POST.get('title'),
                text= request.POST.get('text'),
                user= request.user,
            )
            messages.success(request, 'Post creado')
            return redirect('/')
        else:
            p = Post.objects.get(id = id)
            if (p.user == request.user):
                p.title = request.POST.get('title')
                p.text = request.POST.get('text')
                p.save()
            messages.success(request, 'Post editado')
            return redirect('/')

    context = {}
    if id is not None:
        p = Post.objects.get(id = id)
        context['post'] = p

    return render(request, 'post.html', context)

def commentPage(request):
    p = Post.objects.get(id = request.POST.get('post'))
    Comment.objects.create(
        text= request.POST.get('text'),
        user= request.user,
        post = p,
    )
    return redirect('/')

def coment(request, id = None):
    posts = Post.objects.get(id = id)
    return render(request, 'coment.html', {'posts': posts}) 

def caballoPage(request):
    posts = Caballos.objects.all() 
    return render(request, 'caballo.html', {'posts': posts})

def baqueroPage(request):
    posts = Baqueros.objects.all() 
    return render(request, 'baquero.html', {'posts': posts})

def florafaunaPage(request):
    posts = FloraFauna.objects.all()
    return render(request, 'flofau.html', {'posts': posts})