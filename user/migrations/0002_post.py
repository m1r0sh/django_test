# Generated by Django 4.1.3 on 2022-12-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='theme')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
            ],
        ),
    ]
