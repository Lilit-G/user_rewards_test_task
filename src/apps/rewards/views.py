from rest_framework.generics import ListAPIView
from .serializers import ScheduledRewardSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils.timezone import now, timedelta
from .models import ScheduledReward, RewardLog


class ScheduledRewardListAPIView(ListAPIView):
    serializer_class = ScheduledRewardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ScheduledReward.objects.filter(user=self.request.user).order_by('execute_at')


class RequestRewardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        last_reward = RewardLog.objects.filter(user=user).order_by('-given_at').first()
        if last_reward and last_reward.given_at > now() - timedelta(days=1):
            return Response({"detail": "You have already received a reward within the last 24 hours."},
                            status=status.HTTP_400_BAD_REQUEST)

        ScheduledReward.objects.create(
            user=user,
            amount=10,
            execute_at=now() + timedelta(minutes=5)
        )

        return Response({"detail": "The reward will be issued after 5 minutes."}, status=status.HTTP_201_CREATED)