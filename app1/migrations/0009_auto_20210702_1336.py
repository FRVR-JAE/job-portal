# Generated by Django 3.2.3 on 2021-07-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_worker_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='fb',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='insta',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='post',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/'),
        ),
        migrations.AddField(
            model_name='worker',
            name='twt',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
