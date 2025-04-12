from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = 'src.apps.rewards'
    label = 'rewards'

    def ready(self):
        import src.apps.rewards.signals
        self.verbose_name = _('Rewards')
