from django.db import models
from django.conf import settings

class ScheduledReward(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scheduled_rewards',
        verbose_name='User'
    )
    amount = models.IntegerField(verbose_name='Reward Amount')
    execute_at = models.DateTimeField(verbose_name='Executed')

    def __str__(self):
        return f"Reward for {self.user.username} ({self.amount}) at {self.execute_at}"
