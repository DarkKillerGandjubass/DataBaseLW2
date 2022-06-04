from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import KinoForm, UserForm, LoginForm, UpdateFilms
from django.views.generic import DeleteView, UpdateView, ListView
from django.db.models import Q


class FilterView:
    def get_genres(self):
        return Zhanr.objects.all()

    def get_years(self):
        return Kino.objects.values("year")

class DeleteFilms(DeleteView):
    template_name = 'main/deletefilms.html'
    model = Kino
    success_url = reverse_lazy('enter')


class UpdateFilms(UpdateView):
    template_name = 'main/updatefilms.html'
    model = Kino
    form = UpdateFilms
    fields = ["title", "desc", "genres", "studio", "type"]
    success_url = reverse_lazy('enter')


class FilterMoviesView(FilterView, ListView):
    def get_queryset(self):
        queryset = Kino.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset

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


class EnterView(FilterView, ListView):
    model = Kino
    template_name = 'main/kino_list.html'
    context_object_name ='kino_list'


# def enter(request):
#     data = Kino.objects.all()
#     return render(request, 'main/kino_list.html', {'title': 'Главная страница сайта', 'kinos': data})


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
