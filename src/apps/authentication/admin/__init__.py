from django.contrib import admin
from django.contrib.auth.models import Group

from . import models as admin_models
from src.apps.authentication import models

admin.site.register(models.User, admin_models.UserAdminModel)
admin.site.unregister(Group)

