from django.urls import path
from . import views


app_name = 'voluntarios'

urlpatterns = [
    path('', views.voluntarios, name='voluntarios'),
]
