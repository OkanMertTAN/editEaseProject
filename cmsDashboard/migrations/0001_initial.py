# Generated by Django 5.1.4 on 2025-01-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainText', models.CharField(max_length=200)),
                ('mainDescText', models.TextField()),
            ],
        ),
    ]
