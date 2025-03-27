from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/images', verbose_name='Превью', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    flag_publication = models.BooleanField(default=True, verbose_name='Опубликовать')
    counter_views = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}: {self.content}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title']
