# Generated by Django 5.1.4 on 2025-01-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parfumuri', '0002_perfume_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='notes',
        ),
        migrations.AddField(
            model_name='perfume',
            name='base_notes',
            field=models.ManyToManyField(related_name='base_notes', to='parfumuri.note'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='middle_notes',
            field=models.ManyToManyField(related_name='middle_notes', to='parfumuri.note'),
        ),
        migrations.AddField(
            model_name='perfume',
            name='top_notes',
            field=models.ManyToManyField(related_name='top_notes', to='parfumuri.note'),
        ),
    ]
