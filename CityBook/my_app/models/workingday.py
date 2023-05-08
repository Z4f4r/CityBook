from django.db import models


class WorkingDay(models.Model):
    class Status(models.TextChoices):
        week_1 = 'Mon-Sat', 'Monday-Saturday'
        week_2 = 'Mon-Fri', 'Monday-Friday'
    weekday = models.CharField(max_length=7,
                               choices=Status.choices,
                               default=Status.week_1)

    class Meta:
        verbose_name = "Рабочие день"
        verbose_name_plural = "Рабочие дни"

    def __str__(self):
        return self.weekday
