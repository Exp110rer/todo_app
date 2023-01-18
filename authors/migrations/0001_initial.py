# Generated by Django 4.1.5 on 2023-01-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name="Author's first name")),
                ('last_name', models.CharField(max_length=64, verbose_name="Author's last name")),
                ('birthday_year', models.PositiveIntegerField(verbose_name="Author's birthday year")),
            ],
        ),
    ]