# Generated by Django 4.1.7 on 2023-02-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=255)),
                ('dept_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetails',
        ),
    ]
