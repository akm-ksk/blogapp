from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(verbose_name='タグ名', max_length=30)
  slug = models.SlugField(verbose_name='URL', unique=True)

  def __str__(self):
    return self.name



class Category(models.Model):
  name = models.CharField(verbose_name='カテゴリー名', max_length=30)
  slug = models.SlugField(verbose_name='URL', unique=True)

  def __str__(self):
    return self.name




class Post(models.Model):
  title = models.CharField(verbose_name='タイトル', max_length=100)
  pic = models.ImageField(verbose_name='画像',upload_to='upload', null=False, blank=False)
  text = models.TextField(verbose_name='本文', blank=False)
  create_day = models.DateTimeField(auto_now_add=True)
  update_day = models.DateTimeField(auto_now=True)
  publish = models.BooleanField(verbose_name='公開', default=True)
  tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
  category = models.ForeignKey(Category, verbose_name='カテゴリー', null=True, blank=True, on_delete=models.PROTECT)

  def __str__(self):
    return self.title