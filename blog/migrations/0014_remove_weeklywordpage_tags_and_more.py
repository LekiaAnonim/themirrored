# Generated by Django 4.2.5 on 2023-12-10 18:26

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_subscribeformpage_subscribeformsettings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklywordpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='weeklywordpage',
            name='word_author',
        ),
        migrations.RemoveField(
            model_name='weeklywordpage',
            name='word_category',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='post_title',
            field=models.CharField(blank=True, help_text='Enter the title of your post', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='howpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='howpage',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='howpage',
            name='post_title',
            field=models.CharField(blank=True, help_text='Enter the title of your post', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subscribeformfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='blog.subscribeformpage'),
        ),
        migrations.AlterField(
            model_name='weeklywordpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weeklywordpage',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='weeklywordpage',
            name='post_title',
            field=models.CharField(blank=True, help_text='Enter the title of your post', max_length=500, null=True),
        ),
    ]
