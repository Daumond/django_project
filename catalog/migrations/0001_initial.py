# Generated by Django 5.0.3 on 2024-03-29 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='превью')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='последнее изменение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]