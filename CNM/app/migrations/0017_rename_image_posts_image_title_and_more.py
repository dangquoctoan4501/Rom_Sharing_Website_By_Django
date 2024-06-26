# Generated by Django 5.0.4 on 2024-05-10 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_posts_images1_alter_posts_images2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='image',
            new_name='image_title',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='images1',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='images2',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='images3',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='images4',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='images5',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.posts')),
            ],
        ),
    ]
