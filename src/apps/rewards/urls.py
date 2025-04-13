from django.urls import path

from src.apps.rewards.views import ScheduledRewardListAPIView, RequestRewardView

urlpatterns = [
    path('', ScheduledRewardListAPIView.as_view(), name='reward-list'),
    path("request/", RequestRewardView.as_view(), name="request-reward"),
]
