# Generated by Django 3.1.7 on 2021-11-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211025_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
