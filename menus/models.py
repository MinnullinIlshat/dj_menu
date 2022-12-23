from django.db import models


class Menu(models.Model):
    name = models.CharField("Название", max_length=100)
    url = models.CharField("Ссылка", max_length=255)
    parent = models.CharField("Имя родителя", max_length=100, default='')

    position = models.PositiveIntegerField("Позиция", default=1)
    level = models.PositiveIntegerField("Уровень вложенности", default=0)
    top_level = models.PositiveIntegerField("Позиция корня", default=1)

    def __str__(self):
        return self.name 

    class Meta: 
        ordering = ('top_level', 'level', 'position')
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'