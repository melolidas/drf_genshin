# Generated by Django 4.1.5 on 2023-01-19 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(db_index=1, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_element', models.CharField(db_index=1, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('story', models.TextField(blank=1)),
                ('photo', models.ImageField(blank=1, upload_to='images/', verbose_name='Изображение')),
                ('country', models.ForeignKey(null=1, on_delete=django.db.models.deletion.PROTECT, to='heroes.country')),
                ('element', models.ForeignKey(null=1, on_delete=django.db.models.deletion.PROTECT, to='heroes.element')),
            ],
        ),
    ]
