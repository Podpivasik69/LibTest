from django.db import models
from library.models import Book
from django.urls import reverse

class Provider(models.Model):
    name = models.CharField(max_length=50)
    agent_full_name = models.CharField(max_length=255)
    agent_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('provider_detail', args=[str(self.pk)])

class Deliveries(models.Model):
    delivery_number = models.CharField(max_length=255, verbose_name='Номер поставки')
    delivery_data = models.DateField(verbose_name='Дата поставки')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, )
    delivery_item = models.ForeignKey('library.Book', on_delete=models.CASCADE, )
    delivery_price = models.FloatField(verbose_name='Цена')
    delivery_count = models.FloatField(default=1, verbose_name='Количество поставок')

    def __str__(self):
        return self.delivery_number

    def get_absolute_url(self):
        return reverse ('deliveries_detail', args=[str(self.pk)])