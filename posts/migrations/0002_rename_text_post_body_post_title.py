# Generated by Django 5.0.2 on 2024-03-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default='hi'),
        ),
    ]
