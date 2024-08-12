from django.urls import path
from .views import index, users, show_bio,cinema

urlpatterns = [

    path('users/', users, name='users'),
    path('bio/', show_bio, name='show_bio'),
    path('cinema/', cinema, name='cinema'),
    path('', index, name='homepage'),
    path('sign_in/', sign_in, name='user_loging'),
    path('logout/', logout, name='logout')
]
