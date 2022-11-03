from django.shortcuts import render

# Create your views here.
from .models import Board
def index(request) :
    board_list = Board.objects.all().arder_by('-id')
    context = {'board_list' : '테스트입니다.'}
    return render(request, 'borameboard/index.html', context)
