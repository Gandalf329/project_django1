# Generated by Django 3.1.7 on 2021-04-17 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='title',
            new_name='tittle',
        ),
    ]
