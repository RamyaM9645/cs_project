# Generated by Django 5.1 on 2024-11-09 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenti', '0002_remove_alumnidetails_alumni_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=20)),
                ('enrollment_year', models.IntegerField()),
                ('current_year', models.IntegerField()),
                ('expected_graduation_year', models.IntegerField()),
                ('role_type', models.CharField(choices=[('First Year', 'First Year'), ('Final Year', 'Final Year')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
