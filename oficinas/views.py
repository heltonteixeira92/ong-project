from django.shortcuts import render


def oficinas(requests):
    return render(requests, 'oficinas.html')
