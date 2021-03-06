from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва новини')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    upload_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    photo = models.ImageField(upload_to='photos/%Y/%n/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-create_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
