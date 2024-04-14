from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    date_modified = models.DateTimeField(auto_now=True, verbose_name='последнее изменение', **NULLABLE)
    publication_sign = models.TextField(verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
