# Generated by Django 5.1.2 on 2024-11-05 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSuggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('suggested_flavor', models.CharField(max_length=100)),
                ('suggestion_reason', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('stock', models.FloatField(help_text='grams or units')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonFlavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllergyConcern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concern_detail', models.TextField(help_text='Details about the allergy concern')),
                ('customer_suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergy_concerns', to='choco_app.customersuggestions')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergy_issues', to='choco_app.ingredients')),
            ],
        ),
    ]
