from .models import *
from django.forms import *


class KinoForm(ModelForm):
    class Meta:
        model = Kino
        fields = ["title", "desc", "genres", "studio", "type", "year"]
        title = CharField(max_length=100)
        desc = CharField(max_length=100)
        genres = ModelMultipleChoiceField(queryset=Zhanr.objects.all(), widget=CheckboxSelectMultiple())
        CHOICES_STUDIO = ((i.id, i.name) for i in Studio.objects.all())
        studio = MultipleChoiceField(choices=CHOICES_STUDIO, widget=CheckboxSelectMultiple)
        CHOICES_KINOTYPE = ((i.id, i.typename) for i in KinoType.objects.all())
        type = MultipleChoiceField(choices=CHOICES_KINOTYPE, widget=CheckboxSelectMultiple)
        year = IntegerField()

        # widgets = {
        #     "title": TextInput(attrs={
        #         'class': 'form-row',
        #         'placeholder': 'Введите название плейлиста'
        #     }),
        #     "desc": Textarea(attrs={
        #         'class': 'form-row',
        #         'placeholder': 'Введите описание'
        #     }),
        #     "zhanr": CheckboxInput(attrs={
        #         'class': 'form-row',
        #         'placeholder': 'выберите жанр'
        #     }),
        # }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["login", "password"]
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-row',
                'placeholder': 'Введите логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-row',
                'placeholder': 'Введите пароль',
                'type': 'password'
            }),
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["login", "password"]
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-row',
                'placeholder': 'Введите логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-row',
                'placeholder': 'Введите пароль',
                'type': 'password'
            }),
        }


class UpdateFilms(ModelForm):
    class Meta:
        model = Kino
        fields = ["title", "desc", "genres", "studio", "type", "year"]
        title = CharField(max_length=100)
        desc = CharField(max_length=100)
        genres = ModelMultipleChoiceField(queryset=Zhanr.objects.all(), widget=CheckboxSelectMultiple())
        CHOICES_STUDIO = ((i.id, i.name) for i in Studio.objects.all())
        studio = MultipleChoiceField(choices=CHOICES_STUDIO, widget=CheckboxSelectMultiple())
        CHOICES_KINOTYPE = ((i.id, i.typename) for i in KinoType.objects.all())
        type = MultipleChoiceField(choices=CHOICES_KINOTYPE, widget=CheckboxSelectMultiple())
        year = IntegerField()