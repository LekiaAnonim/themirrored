# Generated by Django 4.2.5 on 2023-12-11 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_weeklywordpage_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importantpages',
            old_name='video_index_page',
            new_name='resources_index_page',
        ),
    ]
