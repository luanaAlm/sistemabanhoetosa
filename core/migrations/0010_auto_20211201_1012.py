# Generated by Django 3.1.7 on 2021-12-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211112_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='category_Animal',
            new_name='Raca_Animal',
        ),
        migrations.RenameField(
            model_name='banhoetosa',
            old_name='category',
            new_name='servicos',
        ),
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
