from functools import reduce
from django.shortcuts import redirect, render
from main import models
from main import forms


# Create your views here.
def index(request):
    articles = models.Article.objects.all().order_by("-createdAt")[:10]
    return render(request, "main/index.html", {"articles": articles})


def article(request, id):
    article = models.Article.objects.get(id=id)
    return render(request, "main/article.html", {"article": article})


def author(request, id):
    author = models.Author.objects.get(id=id)
    return render(request, "main/author.html", {"author": author})


def add_article(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.ArticleForm()
    return render(request, "main/add.html", {"form": form})


def edit_article(request, id):
    article = models.Article.objects.get(id=id)
    if request.method == "POST":
        form = forms.ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.ArticleForm(instance=article)
    return render(request, "main/add.html", {"form": form})


def add_author(request):
    if request.method == "POST":
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.AuthorForm()
    return render(request, "main/add.html", {"form": form})


def edit_author(request, id):
    author = models.Author.objects.get(id=id)
    if request.method == "POST":
        form = forms.AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, "main/add.html", {"form": form})
