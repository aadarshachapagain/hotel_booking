from django.db import models
from django.utils import timezone
from account.models import User


class PasswordReset(models.Model):
    code = models.IntegerField(max_length=6, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name_plural = "Password Reset"
 