from django.urls import path
from .import views

urlpatterns = [
    path('', views.user_author_sign_in, name='user_author_sign_in'),
    path('user_author_login', views.user_author_login, name='user_author_login')
]
