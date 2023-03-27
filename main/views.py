from django.shortcuts import render, redirect
from .models import  Article
from django.http import HttpResponse
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    articles = Article.objects.filter(is_active=True)
    return render(request, 'home.html', {'articles':articles})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    articles = Article.objects.filter(is_active=True)
    return render(request, 'detail.html', {'article':article, 'articles':articles })

def article_create(request):
    user = request.user
    if user.is_authenticated:
        form = ArticleForm()
        if request.method == "POST":
            form = ArticleForm(data= request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = user
                form.save(commit=True)
                return redirect('index')
            else:return render(request, 'create.html', {'form':form})    
        else:return render(request, 'create.html', {'form':form})    
    else:return HttpResponse("Not allowed")
    
def article_update(request, id):
    user = request.user
    article = Article.objects.get(id=id)
    if user == article.author:
        form = ArticleForm(instance=article)
        if request.method == "POST":
            form = ArticleForm(instance=article, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("OK")
            else: return render(request, 'update.html', {'form':form, "article":article})
        else: return render(request, 'update.html', {'form':form, 'article':article})
    else:return HttpResponse("Not allowed")
    
def article_delete(request, id):
    user = request.user
    article = Article.objects.get(id=id)   
    if user == article.author:
        if request.method == "POST":
            article.delete()
            return HttpResponse("OK")
        return render(request, 'delete.html', {"article":article})   
    else:return HttpResponse("Not allowed")