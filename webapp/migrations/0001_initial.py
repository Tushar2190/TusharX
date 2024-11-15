# Generated by Django 5.1.3 on 2024-11-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=125)),
            ],
        ),
    ]
