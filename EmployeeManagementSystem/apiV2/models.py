# from django.db import models

# Create your models here.
# from ..apiV1.models import Employee2
from django.apps import apps

# from apiV1.models import Employee2, Role2, Department2


Employee2 = apps.get_model(
    app_label='apiV1', model_name='Employee2', require_ready=False)
Department2 = apps.get_model(
    app_label='apiV1', model_name='Department2', require_ready=False)
Role2 = apps.get_model(
    app_label='apiV1', model_name='Role2', require_ready=False)
