# Generated by Django 4.2.5 on 2023-09-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=128)),
                ('prix', models.IntegerField()),
                ('quantite', models.IntegerField()),
            ],
        ),
    ]
