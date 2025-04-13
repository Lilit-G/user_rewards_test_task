
from django.urls import path

from src.apps.rewards.views import ScheduledRewardListAPIView

urlpatterns = [
    path('', ScheduledRewardListAPIView.as_view(), name='reward-list'),
]
