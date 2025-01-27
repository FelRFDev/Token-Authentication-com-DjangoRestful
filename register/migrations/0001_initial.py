# Generated by Django 4.0.3 on 2024-05-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('adress', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Registration forms',
            },
        ),
    ]
