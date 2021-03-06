from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import KinoForm, UserForm, LoginForm, UpdateFilms
from django.views.generic import DeleteView, UpdateView, ListView
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


class FilterView:
    def get_genres(self):
        return Zhanr.objects.all()

    def get_years(self):
        return Kino.objects.values("year").distinct()

    def get_types(self):
        return KinoType.objects.all()

    def get_studios(self):
        return Studio.objects.all()


class DeleteFilms(DeleteView):
    template_name = 'deletefilms.html'
    model = Kino
    success_url = reverse_lazy('enter')


class UpdateFilms(UpdateView):
    template_name = 'updatefilms.html'
    model = Kino
    form = UpdateFilms
    fields = ["title", "desc", "genres", "studio", "type"]
    success_url = reverse_lazy('enter')


class FilterMoviesView(FilterView, ListView):
    def get_queryset(self):
        queryset = Kino.objects.all()
        if self.request.GET.getlist("year"):
            queryset = queryset.filter(Q(year__in=self.request.GET.getlist("year")))
        if self.request.GET.getlist("genre"):
            queryset = queryset.filter(Q(genres__in=self.request.GET.getlist("genre")))
        if self.request.GET.getlist("type"):
            queryset = queryset.filter(Q(type__in=self.request.GET.getlist("type")))
        if self.request.GET.getlist("studio"):
            queryset = queryset.filter(Q(studio__in=self.request.GET.getlist("studio")))
        if self.request.GET.getlist("FilmName"):
            queryset = queryset.filter(Q(title__istartswith=self.request.GET.getlist("FilmName")[0]))
        if self.request.GET.getlist("FilmDesc"):
            queryset = queryset.filter(Q(desc__icontains=self.request.GET.getlist("FilmDesc")[0]))
        return queryset.distinct()


def index(request):
    submitButton = request.POST.get("submit")
    loginForm = ''
    passwordForm = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        loginForm = form.cleaned_data.get('username')
        passwordForm = form.cleaned_data.get('password')

    if User.objects.filter(username=loginForm).filter(password=passwordForm):
        uname = loginForm
        upass = passwordForm
        user = authenticate(username=uname, password=upass)
        login(request, user)
        return HttpResponseRedirect(reverse('enter'))

    context = {
        'form': form,
        'submitButton': submitButton,
        'username': loginForm,
        'password': passwordForm
    }
    return render(request, 'index.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def registr(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('enter'))
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'registr.html', context)


class EnterView(FilterView, ListView):
    model = Kino
    template_name = 'main/kino_list.html'
    context_object_name = 'kino_list'

# def enter(request):
#     data = Kino.objects.all()
#     return render(request, 'kino_list.html', {'title': '?????????????? ???????????????? ??????????', 'kinos': data})


def playlist(request):
    error = ''
    if request.method == 'POST':
        form = KinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enter')
        else:
            error = '?????????? ??????????????'

    form = KinoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'playlist.html', context)