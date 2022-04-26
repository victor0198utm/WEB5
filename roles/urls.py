from django.urls import path
from .views import UserEditView, UserRegisterView, dashboard, edit_request

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_request/', edit_request, name='edit_request'),
]