from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ScheduledReward
from .serializers import ScheduledRewardSerializer

class ScheduledRewardListAPIView(ListAPIView):
    serializer_class = ScheduledRewardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ScheduledReward.objects.filter(user=self.request.user).order_by('execute_at')


