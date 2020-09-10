import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.timezone import now

from applications.core.models import Common, PathAndRename


class Slide(Common):
    """
    Слайдер
    """

    title = models.TextField(
        verbose_name='Название',
    ) # yapf: disable

    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('slide'),
        help_text='JPG. 1400x700',
    )

    button_text = models.CharField(
        verbose_name='Текст кнопки',
        max_length=50,
        default='Узнать больше',
    )

    button_url = models.CharField(
        verbose_name='Ссылка кнопки',
        max_length=200,
    )

    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'слайд'
        verbose_name_plural = 'слайдер'

    def thumb_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" width="100">')
    thumb_photo.short_description = 'Превью'

    def __str__(self):
        return self.title


class Index(models.Model):
    """
    Главная страница
    """

    content_1 = RichTextUploadingField(
        verbose_name='Первый контент',
        blank=True,
    )

    content_2 = RichTextUploadingField(
        verbose_name='Второй контент',
        blank=True,
    )

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главная страница'

    def __str__(self):
        return 'Главная страница'


class About(models.Model):
    """
    О компании
    """

    content_1 = RichTextUploadingField(
        verbose_name='Контент (до галереи)',
    ) # yapf: disable

    comment = models.TextField(
        verbose_name='Комментарий (слева)',
        blank=True,
    )

    content_2 = RichTextUploadingField(
        verbose_name='Контент (после галереи)',
        blank=True,
    )

    class Meta:
        verbose_name = 'о компании'
        verbose_name_plural = 'о компании'

    def __str__(self):
        return 'О компании'


class AboutPhoto(models.Model):
    """
    Фото в галерею «О компании»
    """

    about = models.ForeignKey(
        verbose_name='О компании',
        to=About,
        on_delete=models.CASCADE,
        related_name='photos',
    )

    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('main/aboutphoto'),
        help_text='Загружать JPG',
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
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def thumb_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" width="100">')
    thumb_photo.short_description = 'Превью'

    def __str__(self):
        # return self.photo.url
        return '{}'.format(self.pk)


class Page(Common):
    """
    Статическая страница
    """

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
    )

    slug = models.SlugField(
        verbose_name='URL-имя',
        unique=True,
    )

    content = RichTextUploadingField(
        verbose_name='Содержание',
    )

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'статические страницы'

    def get_absolute_url(self):
        return reverse('services:page_detail', kwargs={'slug': self.slug})
    get_absolute_url.short_description = 'Ссылка'

    def __str__(self):
        return self.title


class Preference(models.Model):
    """
    Настройки
    """

    hostname = models.CharField(
        verbose_name='Имя сайта',
        max_length=50,
        blank=True,
        help_text='Например, site.com или localhost:8000',
    )

    phone = models.CharField(
        verbose_name='Телефон',
        max_length=50,
    )

    phone_mobile = models.CharField(
        verbose_name='Телефон (мобильный)',
        max_length=50,
        blank=True,
    )

    phone_whatsapp = models.CharField(
        verbose_name='Whatsapp',
        max_length=50,
        blank=True,
        help_text='Писать в формате "380661234567"',
    )

    phone_viber = models.CharField(
        verbose_name='Viber',
        max_length=50,
        blank=True,
        help_text='Писать в формате "380661234567"',
    )

    address = models.CharField(
        verbose_name='Адрес',
        max_length=200,
    )

    footer_address = models.TextField(
        verbose_name='Адрес (подвал)',
        blank=True,
    )

    map_link = models.CharField(
        verbose_name='Ссылка на проезд к Офису',
        max_length=200,
        blank=True,
    )

    social_facebook = models.CharField(
        verbose_name='Facebook',
        max_length=200,
        blank=True,
    )

    social_vkontakte = models.CharField(
        verbose_name='Vkontakte',
        max_length=200,
        blank=True,
    )

    social_instagram = models.CharField(
        verbose_name='Instagram',
        max_length=200,
        blank=True,
    )

    social_telegram = models.CharField(
        verbose_name='Telegram',
        max_length=200,
        blank=True,
    )

    site_title = models.CharField(
        verbose_name='Заголовок сайта',
        max_length=200,
    )

    site_description = models.TextField(
        verbose_name='Описание сайта',
    )

    site_photo = models.ImageField(
        verbose_name='Изображение для шаринга',
        upload_to=PathAndRename('preference'),
        help_text='Загружать JPG 1200х630',
        blank=True,
    )

    email = models.EmailField(
        verbose_name='Эл.почта',
        max_length=254,
        blank=True,
    )

    email_appointment = models.TextField(
        verbose_name='Емэйлы для заявок "Записаться на встречу"',
        help_text='Каждый емэйл с новой строки',
        blank=True,
    )

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return 'Настройки'
