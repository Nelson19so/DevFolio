# Generated by Django 5.1.4 on 2025-01-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0005_testimonial_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='profile',
            field=models.ImageField(blank=True, default=1, null=True, upload_to='testimonial/'),
        ),
    ]
