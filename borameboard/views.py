from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from .models import Board
from .forms import RegistForm

def index(request) :
    board_list = Board.objects.all().order_by('-id')
    context = {'board_list' : board_list}
    return render(request, 'borameboard/index.html', context)

def regist(request) :
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('borame_board:index')
    else :
        form = RegistForm()
    context = {'form' : form,}
    return render(request, 'borameboard/regist_form.html', context)

def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list' : board_list}
    return render(request, 'borameboard/detail.html', context)

def edit(request, pk):
    post = get_object_or_404(Board, id=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('borame_board:index')
    else:
        form = RegistForm(instance=post)
    context = {'form': form, }
    return render(request, 'borameboard/edit_form.html', context)

def delete(request, pk) :
    post = get_object_or_404(Board, id= pk)
    post.delete()
    return redirect('borame_board:index')
        