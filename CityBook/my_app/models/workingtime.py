from django.db import models


class WorkingTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = "Рабочая время"
        verbose_name_plural = "Рабочие время"
    def __str__(self):
        return f'от {self.start_time} до {self.end_time}'
