# Generated by Django 2.2.4 on 2020-02-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
