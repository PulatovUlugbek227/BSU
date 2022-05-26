from operator import truediv
from tokenize import group
from django.db import models
from django.shortcuts import reverse


class Group(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Owner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    
    def link(self):
        return reverse('student', kwargs={'id': self.id})

class TreeKind(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField('Картинка', blank = True, null = True)


    def __str__(self):
        return self.title

    def link(self):
        return reverse('tree_detail', kwargs = {'id': self.id})

class Area(models.Model):
    polygon = models.TextField()
    sort_num = models.IntegerField()
    square = models.FloatField(default=0)
    id_polygon = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    madaniyat = models.BooleanField(default=False)

    def __str__(self):
        return self.id_polygon

class Tree(models.Model):
    tree_kind = models.ForeignKey(TreeKind, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    latitude = models.FloatField(default=0, blank=True)  #Широта  N or s
    longitude = models.FloatField(default=0, blank=True) #Долгота  E or W
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, blank=True, null=True)

    def link(self):
        return reverse('tree_detail', kwargs = {'id': self.id})

    def __str__(self):
        return self.owner.name
    
class All_Area(models.Model):
    title = models.CharField('Наименование картинки', max_length=255)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField('Фото полигона', upload_to='media/')
    slug = models.SlugField('Сылка на фото', unique=True)

    def get_absolute_url(self):
        return reverse('all_area_detail_url', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Ваши полигон'
        verbose_name_plural = 'Ваши полигоны'

    def __str__(self):
        return self.title
