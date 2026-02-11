from django.db import models

""" ============== Models =============== """
class Cars(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=False)
    