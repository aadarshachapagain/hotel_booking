from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Language"
    #
    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)