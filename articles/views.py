from django.shortcuts import render
from .models import Article
# Create your views here.


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {"articles": articles})


def add_view(request):
    return render(request, 'add.html', {})


def detail_view(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {"article": article})
