# Generated by Django 5.1.3 on 2024-12-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anaBaslik', models.CharField(max_length=200)),
                ('altBaslik', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]