from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    timestamp = models.DateTimeField(verbose_name='Дата')
    
    class Meta:
        ordering = ('-timestamp',)
        verbose_name='Сообщение'
        verbose_name_plural='Блог'
