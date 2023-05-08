from django.db import models


class City(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        ordering = ['title']
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self) -> models.CharField:
        return self.title
