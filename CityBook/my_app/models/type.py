from django.db import models


class Type(models.Model):
    title = models.CharField("Тип",
                             max_length=25)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.title
