from django.shortcuts import render

from news.models import News

def frontpage(request):
    if request.user.is_authenticated:
        news = News.objects.all()
        return render(request, 'core/frontpage.html', {'news': news})
    else:
        news = News.objects.filter(private=False)
        for n in news:
            if n.protected:
                n.description = "Accessible for guests via password."
        return render(request, 'core/frontpage.html', {'news': news})