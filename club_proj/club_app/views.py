from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Comment
from .forms import ClubForm, CommentForm

def index(request):
    clubs = Club.objects.all()
    return render(request, 'index.html', {'clubs':clubs})

def new(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
        club = Club.objects.all().order_by('-id')[0]
        return redirect('detail', club.id)
    else:
        form = ClubForm()
    return render(request, 'new.html', {'form':form})

def detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'club':club, 'comment_form':comment_form})

def comment(request, club_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.club = get_object_or_404(Club, pk=club_id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('detail', club_id)

def update(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST' or request.method == 'FILES':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect('detail', club_id)
    else:
        form = ClubForm(instance=club)

    return render(request, 'update.html', {'form':form})

def delete(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'GET':
        club.delete()
    return redirect('index')

def comment_delete(request, comment_id, club_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'GET':
        comment.delete()
    return redirect('detail', club_id)