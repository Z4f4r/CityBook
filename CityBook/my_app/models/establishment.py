from django.db import models


class Establishment(models.Model):
    title = models.CharField("Название",
                             max_length=25)
    description = models.TextField("Описание",
                                   max_length=300,
                                   blank=True,
                                   null=True)
    address = models.CharField("адрес",
                               max_length=50)
    create_time = models.DateTimeField("Дата создания",
                                       auto_now_add=True)
    update_time = models.DateTimeField("Дата обновления",
                                       auto_now=True)
    photo = models.ImageField("Фото",
                              blank=True,
                              null=True)
    active = models.BooleanField(default=True)
    city = models.ForeignKey("my_app.city",
                             on_delete=models.CASCADE,
                             verbose_name="Город")
    category = models.ForeignKey("my_app.category",
                                 on_delete=models.CASCADE,
                                 verbose_name="Категория")
    contact = models.ForeignKey("my_app.contact",
                                on_delete=models.CASCADE,
                                verbose_name="Контакты")
    working_time = models.ForeignKey("my_app.workingtime",
                                     on_delete=models.CASCADE,
                                     verbose_name="Время работы")
    working_day = models.ForeignKey("my_app.workingday",
                                    on_delete=models.CASCADE,
                                    verbose_name="Рабочие дни")

    class Meta:
        ordering = ['update_time']
        verbose_name = "Учреждение"
        verbose_name_plural = "Учреждения"

    def __str__(self) -> models.CharField:
        return self.title
