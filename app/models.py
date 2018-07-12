from django.db import models
from datetime import datetime

class Histories(models.Model):
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
