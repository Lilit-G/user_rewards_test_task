from celery import shared_task
from django.utils.timezone import now
from .models import ScheduledReward, RewardLog

@shared_task
def process_scheduled_reward(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        if reward.execute_at <= now():
            user = reward.user
            user.coins += reward.amount
            user.save()

            RewardLog.objects.create(
                user=user,
                amount=reward.amount,
                given_at=now()
            )

            reward.delete()
    except ScheduledReward.DoesNotExist:
        pass
