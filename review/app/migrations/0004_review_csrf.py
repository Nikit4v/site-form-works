# Generated by Django 3.0.2 on 2020-02-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='csrf',
            field=models.TextField(blank=True, null=True),
        ),
    ]
