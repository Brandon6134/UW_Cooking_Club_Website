# Generated by Django 4.2.19 on 2025-02-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0003_remove_recipe_cuisine_remove_recipe_meal_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooking_class',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
