from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {"articles": articles})


def add_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add.html', {})


def detail_view(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {"article": article})


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('index')


def edit_view(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', {"article": article})
