# Generated by Django 3.1.7 on 2021-11-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cadastro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='banhoetosa_ptr',
        ),
    ]
