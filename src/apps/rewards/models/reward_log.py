from django.db import models
from django.conf import settings

class RewardLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reward_logs',
        verbose_name='User'
    )
    amount = models.IntegerField(verbose_name='Reward Amount')
    given_at = models.DateTimeField(verbose_name='Given Date')

    def __str__(self):
        return f"RewardLog: {self.user.username} received {self.amount} at {self.given_at}"

