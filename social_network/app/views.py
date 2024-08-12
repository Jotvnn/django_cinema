from django.shortcuts import render
from .models import Genres, Actors, Cinema
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    genres = Genres.objects.all()
    return render(request,template_name='homepage.html',context={'cinema_type': genres})

def cinema(request):
    genres = Genres.objects.all()
    active = genres.first()
    data = []
    if request.GET:
        data = Cinema.objects.filter(genres=Genres.objects.get(name=request.GET['genres']))
        active = request.GET['genres']
    return render(request, 'cinema.html',context={'active':active,'cinema_type': genres,'data':data})

def users(request):
    genres = Genres.objects.all()

    return render(request, 'users.html',context={'cinema_type': genres})

def show_bio(request):
    genres = Genres.objects.all()

    return render(request,'bio.html',context={'cinema_type': genres})

def sign_up(request):
    if request.user.is_authenticate:
        if request['password1']==['password2']:
            user = User.objects.create_user(request['username'], request['email'], request['passord'])
            authenticate(request,user)
            return render(request,'',)
    return render(request, 'sign_up.html')

def user_logout(request):
    pass

def user_reset_password(request):
    pass

def user_personal(request):
    pass

def loging(request):
    if request.POST

        return render(request, 'homepage.html', {"message": f'you are logged in'})

    if request.POST:
        if request.POST['username'] in users:
            log = login(request, request.POST['username'])
            if log:
                return render(request, 'homepage.html',)
    return render(request, 'sign_up')
