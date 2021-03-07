from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News, Category

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {
        'news': news,
        'title': 'Список новин',
        'categories': categories
    })

