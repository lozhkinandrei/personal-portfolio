# Generated by Django 2.2.13 on 2020-06-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200614_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemetadata',
            name='google_tracking_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
