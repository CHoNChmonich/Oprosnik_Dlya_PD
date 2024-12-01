# Generated by Django 5.1.3 on 2024-12-01 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_subject_minimum_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileSubjectMinScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='min_scores', to='profiles.profile')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.subject')),
            ],
        ),
    ]
