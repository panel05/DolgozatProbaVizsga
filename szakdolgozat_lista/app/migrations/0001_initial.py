# Generated by Django 4.2 on 2023-04-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Szakdoga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szakdoga_nev', models.CharField(max_length=50, unique=True, verbose_name='szakdoga_nev')),
                ('githublink', models.CharField(max_length=200, unique=True, verbose_name='githublink')),
                ('oldallink', models.CharField(max_length=200, unique=True, verbose_name='oldallink')),
                ('tagokneve', models.TextField(verbose_name='tagokneve')),
            ],
        ),
    ]
