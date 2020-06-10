from django.db import models
from django.utils import timezone
from datetime import datetime
from django.shortcuts import reverse


class Slide(models.Model):
    title = models.CharField('Title', max_length=150)
    slug = models.SlugField('URL', unique=True)
    summary = models.TextField('Summary', db_index=True, max_length=500)
    date = models.DateTimeField('Date', auto_now_add=True)
    image = models.ImageField('Image')

    def get_absolute_url(self):
        return reverse('slide_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

    def __str__(self):
        return self.title


class Customer(models.Model):
    full_name = models.CharField("Full Name", max_length=50)
    email = models.EmailField('E-mail', db_index=True)
    phone = models.CharField('Phone', max_length=15)
    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.full_name


class Country(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    flag = models.ImageField('Flag')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Tour(models.Model):
    title = models.CharField('Title', max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField('Description', max_length=1000)
    image = models.ImageField('Image')

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.title
