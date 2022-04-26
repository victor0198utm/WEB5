from dataclasses import fields
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponseRedirect
from .forms import ProfileForm, UserForm
from news.models import News

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# def register_user(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return HttpResponseRedirect('/roles/login')
    
#     return render(request, 'news/add.html', {'form':form})

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
        return render(request, 'registration/profile.html', {"profile": {"is_editor": False, "want_to_edit": False}, "news": []})

    try:
        news = News.objects.filter(author=request.user)
        print(news)
    except:
        return render(request, 'registration/profile.html', {"profile": profile, "news": []})

    return render(request, 'registration/profile.html', {"profile": profile, "news": news})

def edit_request(request):
    try:
        profile = Profile.objects.get(user=request.user)
        profile.want_to_edit = True
        profile.save()
    except:
        profile = Profile(user=request.user, want_to_edit=True)
        profile.save()

    return HttpResponseRedirect('/roles/profile/')