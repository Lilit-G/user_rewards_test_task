from django.contrib import admin

class ScheduledRewardAdminModel(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at')
    list_filter = ('user', 'execute_at')
    search_fields = ('user__username',)
    ordering = ('-execute_at',)