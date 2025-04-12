from django.contrib import admin

from . import models as admin_models
from src.apps.rewards import models


admin.site.register(models.ScheduledReward, admin_models.ScheduledRewardAdminModel)
