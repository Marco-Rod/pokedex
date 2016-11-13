# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Abilities',
                'verbose_name': 'Ability',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'verbose_name': 'City',
            },
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Generations',
                'verbose_name': 'Generation',
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.City')),
            ],
            options={
                'verbose_name_plural': 'Gyms',
                'verbose_name': 'Gym',
            },
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Habitats',
                'verbose_name': 'Habitat',
            },
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Liders',
                'verbose_name': 'Lider',
            },
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Medals',
                'verbose_name': 'Medal',
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('power', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Moves',
                'verbose_name': 'Move',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('initial', models.BooleanField()),
                ('legendary', models.BooleanField()),
                ('weight', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('color', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='images/')),
                ('ability', models.ManyToManyField(to='pokemon.Ability')),
                ('generation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Generation')),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Habitat')),
            ],
            options={
                'verbose_name_plural': 'Pokemons',
                'verbose_name': 'Pokemon',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('home', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Professors',
                'verbose_name': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Regions',
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Speciess',
                'verbose_name': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='pokemon.City')),
            ],
            options={
                'verbose_name_plural': 'Towns',
                'verbose_name': 'Town',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('move', models.ManyToManyField(related_name='Moves', to='pokemon.Move')),
            ],
            options={
                'verbose_name_plural': 'Types',
                'verbose_name': 'Type',
            },
        ),
        migrations.AddField(
            model_name='professor',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Region'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Species'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(to='pokemon.Type'),
        ),
        migrations.AddField(
            model_name='lider',
            name='types',
            field=models.ManyToManyField(related_name='Types', to='pokemon.Type'),
        ),
        migrations.AddField(
            model_name='gym',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Lider'),
        ),
        migrations.AddField(
            model_name='gym',
            name='medal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Medal'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='pokemon.Region'),
        ),
    ]