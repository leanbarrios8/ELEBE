from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio/index.html')

def blex(request):
    return render(request, 'inicio/Staking.html')
