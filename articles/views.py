from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.


@login_required(login_url='/login/')
def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {"articles": articles})


@login_required(login_url='/login/')
def add_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'add.html', {'form': form})


@login_required(login_url='/login/')
def edit_view(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article_id = get_object_or_404(Article, id=id)
        form = ArticleForm(
            request.POST, request.FILES, instance=article_id)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'edit.html', {"article": article, 'form': form})


@login_required(login_url='/login/')
def detail_view(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {"article": article})


@login_required(login_url='/login/')
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('index')
