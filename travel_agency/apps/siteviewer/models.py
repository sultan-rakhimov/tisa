from django.db import models
from django.utils import timezone
from datetime import datetime
from django.shortcuts import reverse


class Slide(models.Model):
    title = models.CharField('Title', max_length=150)
    slug = models.SlugField('URL', max_length=150, unique=True)
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
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=20)
    email = models.EmailField('E-mail', db_index=True)
    phone = models.CharField('Phone', max_length=15)
    date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        customer = self.first_name + ' ' + self.last_name
        return customer
