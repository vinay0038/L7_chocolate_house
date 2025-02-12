# Generated by Django 5.1.2 on 2024-11-05 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choco_app', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concern_detail', models.TextField(help_text='Details about the allergy concern')),
            ],
        ),
        migrations.CreateModel(
            name='FlavorSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Inquiry',
        ),
        migrations.RemoveField(
            model_name='allergyconcern',
            name='customer_suggestion',
        ),
        migrations.RemoveField(
            model_name='allergyconcern',
            name='ingredient',
        ),
        migrations.DeleteModel(
            name='SeasonFlavor',
        ),
        migrations.RenameModel(
            old_name='CustomerSuggestions',
            new_name='CustomerSuggestion',
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.AddField(
            model_name='allergyissue',
            name='customer_suggestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergy_issues', to='choco_app.customersuggestion'),
        ),
        migrations.AddField(
            model_name='allergyissue',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergy_problems', to='choco_app.ingredient'),
        ),
        migrations.DeleteModel(
            name='AllergyConcern',
        ),
    ]
