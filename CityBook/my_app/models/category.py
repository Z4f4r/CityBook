from django.db import models


class Category(models.Model):
    title = models.CharField("Название",
                             max_length=25)
    type = models.ForeignKey("my_app.type",
                             on_delete=models.CASCADE,
                             verbose_name="Тип категории")

    class Meta:
        ordering = ['title']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.title} {self.type.title}'
