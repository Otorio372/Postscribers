# Generated by Django 5.0.4 on 2024-09-28 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_postmodel_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
