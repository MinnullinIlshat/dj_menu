# Generated by Django 4.1.4 on 2022-12-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_alter_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='bname',
            field=models.CharField(default='bn', max_length=100, verbose_name='Имя блока'),
        ),
    ]
