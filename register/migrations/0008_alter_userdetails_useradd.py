# Generated by Django 4.0.5 on 2022-06-16 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_remove_userdetails_user_address_userdetails_useradd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='useradd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.useraddresses'),
        ),
    ]
