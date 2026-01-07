from django.db import models


class NewsCategory(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название категории")


    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class News(models.Model):

    title = models.CharField(max_length=255, verbose_name="Заголовок")


    content = models.TextField(verbose_name="Основной текст")


    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name="Категория"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']