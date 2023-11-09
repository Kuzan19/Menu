from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        default='',
        blank=True,
        null=True)

    def __str__(self):
        """Функция отображения объекта"""
        return f'{self.name}'

    def get_url(self):
        """Функция возвращает url объекта (в данном случае обращение по slug)"""
        return reverse("category_page", args=[self.slug])

    def save(self, *args, **kwargs):
        """Функция присваивает slug при сохранении в базу данных объекта"""
        self.slug = slugify(f"{self.name}")
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):

    class Meta:

        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        default='',
        blank=True,
        null=True
    )

    def __str__(self):
        """Функция отображения объекта"""
        return f'{self.name}'

    def get_url(self):
        """Функция возвращает url объекта (в данном случае обращение по slug)"""
        return reverse("subcategory_page", args=[self.slug])

    def save(self, *args, **kwargs):
        """Функция присваивает slug при сохранении в базу данных объекта"""
        if self.parent:
            self.slug = slugify(f"{self.name}-{self.parent}")
        else:
            self.slug = slugify(f"{self.name}")
        super(SubCategory, self).save(*args, **kwargs)



