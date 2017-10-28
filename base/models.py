from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class BlameBaseModel(models.Model):
    created_by = models.ForeignKey(USER_MODEL, related_name='+')
    created = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(USER_MODEL, related_name='+')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
