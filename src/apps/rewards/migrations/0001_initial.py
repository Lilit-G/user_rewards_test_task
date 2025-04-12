# Generated by Django 5.1.8 on 2025-04-12 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Reward Amount')),
                ('given_at', models.DateTimeField(verbose_name='Given Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_logs', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Reward Amount')),
                ('execute_at', models.DateTimeField(verbose_name='Executed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_rewards', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
