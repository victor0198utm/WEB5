from gc import get_objects
from django.shortcuts import render, get_object_or_404

from .models import News
from .forms import NewsForm

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)

    return render(request, 'news/detail.html', {'news':news})

def add(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'news/add.html', {'form':form})
