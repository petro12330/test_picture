from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Файл', blank=True, null=True)
    image_url = models.URLField(blank=True, verbose_name='Ссылка', null=True)

    class Meta:
        verbose_name = 'Изображения'
