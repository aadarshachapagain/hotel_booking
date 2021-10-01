from django.db import models
from datetime import datetime
from users.models import Users

class HotelLog(models.Model):
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    logs = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.logs

    class Meta:
        verbose_name_plural = "Hotel Log"