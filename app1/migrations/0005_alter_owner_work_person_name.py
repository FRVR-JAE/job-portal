# Generated by Django 3.2.3 on 2021-06-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_owner_work_work_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner_work',
            name='person_name',
            field=models.CharField(max_length=100),
        ),
    ]
