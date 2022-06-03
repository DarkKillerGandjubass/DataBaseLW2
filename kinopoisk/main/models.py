from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Studio(models.Model):
    name = models.CharField('название студии', max_length=40)

    def __str__(self):
        return self.name

class KinoType(models.Model):
    typename = models.CharField('выберите тип', max_length=40)

    def __str__(self):
        return self.typename


class Zhanr(models.Model):
    name = models.CharField('жанр', max_length=20)

    def __str__(self):
        return self.name


class Kino(models.Model):
    title = models.CharField('название фильма', max_length=50)
    desc = models.CharField('описание фильма', max_length=300)
    one = models.ForeignKey(Zhanr, on_delete=models.CASCADE, default=None, related_name="one", null=True)
    two = models.ForeignKey(Zhanr, on_delete=models.CASCADE, default=None, related_name="two", null=True)
    three = models.ForeignKey(Zhanr, on_delete=models.CASCADE, default=None, related_name="three", null=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, default=None, related_name="studio")
    type = models.ForeignKey(KinoType, on_delete=models.CASCADE, default=None, related_name="type")
    year = models.IntegerField(default=2000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'


class User(models.Model):
    login = models.CharField('логин', max_length=20)
    password = models.CharField('пароль', max_length=30)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class ZhanrKino(models.Model):
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
