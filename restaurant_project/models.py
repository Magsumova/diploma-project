from turtle import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

# class CustomUser(AbstractUser):
#   bio = models.TextField(verbose_name='Биография пользователя', blank=True)
#   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Зарегистрирован пользователь')
#   updated_at = models.DateTimeField(auto_now = True, verbose_name = "Обновление пользователя")
#   author = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Аватарка пользователя', blank=True)
#   country = models.CharField(max_length=35, verbose_name='Страна')

class Category(models.Model):
  name = models.CharField(max_length=255, verbose_name="Названия категорий")
  url = models.URLField(verbose_name='Иконка категорий', null=True)

  def __str__(self):
    return self.name 

  class Meta:
    verbose_name='Категория блюдо'
    verbose_name_plural='Категорий блюдо'

class Menu(models.Model):
  name = models.CharField(max_length=255, verbose_name='Название блюдо')
  content = models.TextField(verbose_name='О блюдо')
  price = models.IntegerField(verbose_name='Цена блюдо')
  photo = models.URLField(verbose_name='Фотография блюдо', null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорий блюдо', null=True)
  url = models.SlugField(max_length=25, null=True)

  def __str__(self) -> str:
       return self.name 

  def get_absolute_url(self):
      return reverse("view_dish", kwargs={"slug": self.url})
  

  class Meta:
    verbose_name = 'Меню'
    verbose_name_plural = 'Меню'


class Review(models.Model):
  name = models.CharField(max_length=255, verbose_name='Имя')
  email = models.EmailField(verbose_name='Почта')
  text = models.TextField(verbose_name='Сообщение', max_length=5000)
  created_at = models.DateTimeField(auto_now_add=True, null=True)


  def __str__(self):
    return self.name 

  class Meta:
    verbose_name='Отзыв'
    verbose_name_plural='Отзывы'