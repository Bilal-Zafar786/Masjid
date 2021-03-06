# Generated by Django 3.2.8 on 2021-10-15 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('roll_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=30)),
                ('addmission_date', models.DateField()),
                ('promised_fee', models.IntegerField()),
            ],
            options={
                'db_table': 'student_registration',
            },
        ),
        migrations.CreateModel(
            name='Student_Progress1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('month', models.DateField()),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Masjid1.student_registration')),
            ],
            options={
                'db_table': 'student_progress1',
            },
        ),
    ]
