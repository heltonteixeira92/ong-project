from django.shortcuts import render


def voluntarios(requests):
    return render(requests, 'voluntarios.html')
