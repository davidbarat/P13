# Generated by Django 3.1.7 on 2021-04-11 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0002_auto_20210411_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='help.group'),
            preserve_default=False,
        ),
    ]
