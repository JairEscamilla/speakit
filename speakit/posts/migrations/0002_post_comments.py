# Generated by Django 3.0.8 on 2020-08-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_remove_comment_post'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='comments_posts', to='comments.Comment'),
        ),
    ]
