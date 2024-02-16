# Generated by Django 5.0.2 on 2024-02-16 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('last_login', models.DateTimeField()),
                ('is_deleted', models.BooleanField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conn_id', models.CharField(max_length=50)),
                ('since', models.DateTimeField()),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='alumni.alumni')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='alumni.alumni')),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conn_req_id', models.CharField(max_length=50)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='alumni.alumni')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='alumni.alumni')),
            ],
        ),
        migrations.CreateModel(
            name='EduDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_id', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('entry_date', models.DateField()),
                ('passout_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni.alumni')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_id', models.CharField(max_length=50)),
                ('orgname', models.CharField(max_length=100)),
                ('ocupation', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('alunmi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni.alumni')),
            ],
        ),
    ]