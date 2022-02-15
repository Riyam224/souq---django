import imp
from urllib.parse import urlparse
from django.urls import path
from . import views 




urlpatterns = [
    path('signup',views.signup , name='signup' ),
    path('profile/<slug:slug>',views.profile , name='profile' ),
]
