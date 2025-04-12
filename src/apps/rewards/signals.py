from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ScheduledReward
from .tasks import process_scheduled_reward

@receiver(post_save, sender=ScheduledReward)
def schedule_task_on_create(sender, instance, created, **kwargs):
    if created:
        process_scheduled_reward.apply_async(
            args=[instance.id],
            eta=instance.execute_at
        )
