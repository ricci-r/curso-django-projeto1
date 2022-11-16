# Generated by Django 4.1.2 on 2022-11-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                default="recipes/covers/default.png",
                upload_to="recipes/covers/%Y/%m/%d/",
            ),
        ),
    ]