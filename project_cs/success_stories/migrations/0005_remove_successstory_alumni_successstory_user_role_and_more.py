# Generated by Django 5.1 on 2024-11-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0004_remove_successstory_alumni_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstory',
            name='alumni',
        ),
        migrations.AddField(
            model_name='successstory',
            name='user_role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='successstory',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
