from django.urls import path
from . import views

app_name = 'oficinas'

urlpatterns = [
    path('', views.oficinas, name='oficinas'),
]
