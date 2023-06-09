# Generated by Django 4.2.1 on 2023-05-08 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_type_workingtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, verbose_name='уникальный ник')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('surname', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('phone_1', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('phone_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Дополнительный номер')),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.type', verbose_name='Тип категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
    ]
