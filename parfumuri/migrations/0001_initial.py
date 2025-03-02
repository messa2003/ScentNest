# Generated by Django 5.1.4 on 2024-12-10 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brandID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('noteID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('perfumeID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin'), ('U', 'Unisex')], max_length=10)),
                ('description', models.TextField()),
                ('concentration', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('recommended_price', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfumes', to='parfumuri.brand')),
                ('notes', models.ManyToManyField(related_name='perfumes', to='parfumuri.note')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('admin', models.BooleanField(default=False)),
                ('favoriteNotes', models.ManyToManyField(blank=True, related_name='favorited_by', to='parfumuri.note')),
                ('favoritePerfumes', models.ManyToManyField(blank=True, related_name='favorited_by', to='parfumuri.perfume')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
                ('reviewTitle', models.CharField(max_length=100)),
                ('reviewComment', models.TextField()),
                ('perfume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='parfumuri.perfume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='parfumuri.user')),
            ],
        ),
    ]
