from django.shortcuts import render

from news.models import News

def frontpage(request):
    news = News.objects.all()
    return render(request, 'core/frontpage.html', {'news': news})
