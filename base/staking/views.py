from django.shortcuts import render
from django.views.generic.list import ListView


def staking(request):
    return render(request, 'staking/staking.html')
