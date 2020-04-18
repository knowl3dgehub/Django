from .models import MyUser
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AdminForm


def login_view(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'admin_login.html')
        else:
            return redirect('/dashboard/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'admin_login.html', context={'message': 'Invalid username or password'})

class DashboardListView(ListView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    model = MyUser
    template_name = 'dashboard.html'

class AdminCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    model = MyUser
    form_class = AdminForm
    template_name = 'create_admin.html'
    success_url = '/list_admin'

class AdminListView(LoginRequiredMixin, ListView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    model = MyUser
    template_name = 'list_admin.html'
    paginate_by = 10
    ordering = 'id'

class AdminDetailView(LoginRequiredMixin, DetailView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    model = MyUser
    template_name = 'details_admin.html'
    success_url = '/list_admin'


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    form_class = AdminForm
    model = MyUser
    template_name = 'update_admin.html'
    success_url = '/list_admin'


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin_login/'
    redirect_field_name = 'redirect_to'
    model = MyUser
    template_name = 'delete_admin.html'
    success_url = '/list_admin'