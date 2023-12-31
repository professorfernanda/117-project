# Generated by Django 4.2.7 on 2023-11-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('period', models.CharField(max_length=50)),
                ('technologies', models.ManyToManyField(to='experiences.tech')),
            ],
        ),
    ]
