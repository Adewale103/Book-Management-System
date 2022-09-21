from django.contrib.admin.apps import AdminConfig
from .admin import DjangoProject3AdminSite


class DjangoProject3AdminConfig(AdminConfig):
    default_site = "djangoProject3.admin.DjangoProject3AdminSite"

