# Generated by Django 4.0.4 on 2023-02-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrappingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
