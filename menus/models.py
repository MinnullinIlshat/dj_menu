from django.db import models


class Menu(models.Model):
    name = models.CharField("Название", max_length=100)
    url = models.CharField("Ссылка", max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, 
        related_name='child', on_delete=models.CASCADE)

    top_position = models.PositiveIntegerField("Позиция главного пункта", default=0)
    position = models.PositiveIntegerField("Позиция", default=1)
    lvl = models.PositiveIntegerField("Уровень", default=0)

    def __str__(self):
        return self.name 

    class Meta: 
        ordering = ('top_position', 'lvl', 'position')
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'