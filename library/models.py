from django.db import models

class Author(models.Model):
    title = models.CharField(max_length=150, verbose_name='ФИО Автора', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название книги')
    description = models.TextField(blank=True, null=True, verbose_name='Описание книги')
    count_pages = models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')
    price = models.FloatField(verbose_name='Цена')
    cover_type = models.CharField(max_length=150, null=True, verbose_name='Тип обложки')
    size = models.CharField(max_length=150, null=True, verbose_name='Размер книги')
    publication_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='images/', null=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
