# Generated by Django 2.0.2 on 2018-09-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0010_submission_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_title',
            field=models.CharField(max_length=100),
        ),
    ]