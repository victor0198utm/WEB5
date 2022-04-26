from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseRedirect
from .forms import UserForm
from news.models import News

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('frontpage')

    def get_object(self):
        return self.request.user

def dashboard(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return render(request, 'registration/dashboard.html', {"profile": {"is_editor": False, "want_to_edit": False}, "news": []})

    try:
        news = News.objects.filter(author=request.user)
        print(news)
    except:
        return render(request, 'registration/dashboard.html', {"profile": profile, "news": []})

    return render(request, 'registration/dashboard.html', {"profile": profile, "news": news})

def edit_request(request):
    try:
        profile = Profile.objects.get(user=request.user)
        profile.want_to_edit = True
        profile.save()
    except:
        profile = Profile(user=request.user, want_to_edit=True)
        profile.save()

    return HttpResponseRedirect('/roles/dashboard/')