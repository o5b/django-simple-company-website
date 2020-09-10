import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

from applications.core.models import Common, PathAndRename


class Service(Common):
    """
    Услуги
    """

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    slug = models.SlugField(
        verbose_name='URL-имя',
        unique=True,
    )

    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('services/service/photo'),
        blank=True,
        null=True,
        help_text='JPG. 1040x500px',
    )

    content = RichTextUploadingField(
        verbose_name='Контент',
    ) # yapf: disable

    conclusion = RichTextUploadingField(
        'Контент (после прайса)',
        blank=True,
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def get_photo(self):
        if self.photo:
            return self.photo
        media_photo = self.media.filter(photo__isnull=False).first()
        if media_photo:
            return media_photo.photo
        return None

    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Media(models.Model):
    """
    Медиа: Фото / Видео
    """

    service = models.ForeignKey(
        verbose_name='Услуга',
        to=Service,
        on_delete=models.CASCADE,
        related_name='media',
    )

    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('services/photo'),
        help_text='JPG. 1200px по большей стороне',
    )

    youtube_link = models.CharField(
        verbose_name='Ссылка на видео',
        max_length=200,
        help_text='Ссылка на YouTube',
        blank=True,
    )

    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'медиа'
        verbose_name_plural = 'медиа'

    def clean(self):
        if not self.photo and not self.youtube_link:
            raise ValidationError('Необходимо заполнить либо поле фото, либо ссылку на видео')

    def get_youtube_id(self):
        if 'youtube.com' in self.youtube_link:
            pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
            g = re.search(pattern, self.youtube_link)
            if g:
                return g.groups()[0]
        return self.youtube_link

    def thumb_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="100">')
        return None

    thumb_photo.short_description = 'Превью'

    def __str__(self):
        return 'Медиа #{}'.format(self.id)


class Price(models.Model):
    """
    Цены
    """

    service = models.ForeignKey(
        verbose_name='Услуга',
        to=Service,
        on_delete=models.CASCADE,
        related_name='prices',
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    price = models.CharField(
        verbose_name='Стоимость',
        max_length=50,
    )

    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'прайс'
        verbose_name_plural = 'прайс'

    def __str__(self):
        return self.title


class Popular(Common):
    """
    Популярные услуги
    """

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('services/popular/photo'),
        blank=True,
        null=True,
        help_text='JPG. 400x400',
    )

    link = models.URLField(
        verbose_name='Ссылка',
        max_length=300,
    )

    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'популярная услуга'
        verbose_name_plural = 'популярные услуги'

    def thumb_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="100">')
        return None # yapf: disable
    thumb_photo.short_description = 'Превью'

    def __str__(self):
        return self.title
