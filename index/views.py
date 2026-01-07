from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, 'index/index.html', {'news': news})

def news_detail(request, pk):

    from django.shortcuts import get_object_or_404
    item = get_object_or_404(News, pk=pk)
    return render(request, 'index/detail.html', {'item': item})