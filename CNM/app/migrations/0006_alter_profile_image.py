# Generated by Django 5.0.4 on 2024-05-07 07:07

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_profile_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, default='T:\\CNM_Project\\CNM\\static\\images/profile-icon-design-free-vector.jpg', null=True, upload_to=app.models.use_directory_paths),
        ),
    ]