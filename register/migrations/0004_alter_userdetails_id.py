# Generated by Django 4.0.5 on 2022-06-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_useraddresses_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
