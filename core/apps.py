from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class CoreConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Diamond Hub'
    institution = 'Triallav Holdings'
    disclaimer = 'For Triallav Holdings & it\'s Customers use only.'