# Generated by Django 4.2.4 on 2024-03-29 08:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_writing_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writing',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
