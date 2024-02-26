# Generated by Django 5.0.2 on 2024-02-26 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('comments_reviews', '0001_initial'),
        ('tourist_attractions', '0002_remove_touristspot_comment_touristspot_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address'),
        ),
        migrations.AlterField(
            model_name='touristspot',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments_reviews.comment'),
        ),
    ]
