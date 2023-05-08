from django.db import models


class Contact(models.Model):
    slug = models.SlugField("уникальный ник",
                            max_length=20)
    name = models.CharField("Имя",
                            max_length=25)
    surname = models.CharField("Фамилия",
                               max_length=25)
    description = models.TextField("Дополнительная информация",
                                   blank=True,
                                   null=True)
    phone_1 = models.CharField("Номер телефона",
                               max_length=20)
    phone_2 = models.CharField("Дополнительный номер",
                               max_length=20,
                               blank=True,
                               null=True)
    email = models.EmailField()
    photo = models.ImageField("Фото",
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.slug
