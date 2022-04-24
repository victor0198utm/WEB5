from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import News
from .forms import NewsForm

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)

    return render(request, 'news/detail.html', {'news':news})

def add(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    return render(request, 'news/add.html', {'form':form})

def update(request, slug):
    obj = get_object_or_404(News, slug=slug)
    
    try:
        obj = News.objects.get(slug=slug, author=request.user)
    except:
        return render(request, "news/edit_not_permitted.html")
 
    form = NewsForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+slug)
  
    return render(request, "news/edit.html", {"form":form})
