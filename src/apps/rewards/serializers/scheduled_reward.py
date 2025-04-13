from rest_framework import serializers

from src.apps.rewards.models import ScheduledReward


class ScheduledRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledReward
        fields = ('amount', 'execute_at')


