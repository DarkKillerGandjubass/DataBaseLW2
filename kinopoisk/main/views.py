from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import KinoForm, UserForm, LoginForm, UpdateFilms
from django.views.generic import DeleteView, UpdateView


class DeleteFilms(DeleteView):
    template_name = 'main/deletefilms.html'
    model = Kino
    success_url = reverse_lazy('enter')


class UpdateFilms(UpdateView):
    template_name = 'main/updatefilms.html'
    model = Kino
    form = UpdateFilms
    fields = ["title", "desc", "one", "two", "three", "studio", "type"]
    success_url = reverse_lazy('enter')


def index(request):
    submitButton = request.POST.get("submit")
    loginForm = ''
    passwordForm = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        loginForm = form.cleaned_data.get('login')
        passwordForm = form.cleaned_data.get('password')

    if User.objects.filter(login=loginForm).filter(password=passwordForm):
        return redirect('/enter')

    context = {
        'form': form,
        'submitButton': submitButton,
        'login': loginForm,
        'password': passwordForm
    }
    return render(request, 'main/index.html', context)


def registr(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'main/registr.html', context)


def enter(request):
    data = Kino.objects.all()
    return render(request, 'main/enter.html', {'title': 'Главная страница сайта', 'kinos': data})


def playlist(request):
    error = ''
    if request.method == 'POST':
        form = KinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enter')
        else:
            error = 'форма неверна'

    form = KinoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/playlist.html', context)
