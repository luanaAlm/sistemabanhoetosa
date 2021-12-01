# Generated by Django 3.1.7 on 2021-11-13 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211102_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.animal')),
                ('banhoetosa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.banhoetosa')),
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.pessoa')),
                ('ID_Cadastro', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('core.pessoa', 'core.banhoetosa', 'core.animal'),
        ),
    ]
