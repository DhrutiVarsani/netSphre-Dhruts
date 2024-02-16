# Generated by Django 5.0.2 on 2024-02-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('is_deleted', models.BooleanField()),
            ],
        ),
    ]