from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import News
from .forms import NewsForm

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)

    if not request.user.is_authenticated:
        if news.protected:
            if request.method == 'POST':
                # daca parola e corecta, arata noutatea
                print(request.POST["news_pass"])

                try:
                    news = News.objects.get(slug=slug, password=request.POST["news_pass"])
                    return render(request, 'news/detail.html', {'news':news})
                except:
                    return render(request, 'news/news_password.html', {"slug": slug, "incorrect_password": True})
            else:
                news_title = news.title
                return render(request, 'news/news_password.html', {"news_title": news_title})
        elif news.private:
            return render(request, 'news/private_news.html')
        else:
            return render(request, 'news/detail.html', {'news':news})
    else:
        try:
            News.objects.get(slug=slug, author=request.user)
            return render(request, 'news/detail.html', {'news':news, 'editable': True})
        except:
            pass

        return render(request, 'news/detail.html', {'news':news})

def add(request):
    if not request.user.profile.is_editor:
        print("Is not editor")
        return render(request, 'news/not_an_editor.html')
    else:
        print("Is editor")
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

    if request.method == 'POST':
        form = NewsForm(request.POST or None, request.FILES, instance = obj)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+slug)
    
        return render(request, "news/edit.html", {"form":form})
    
    news = get_object_or_404(News, slug=slug)
    form = NewsForm(instance = news)
    return render(request, "news/edit.html", {"form":form})

