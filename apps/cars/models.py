from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError

""" ============== Models =============== """

def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError('Only alphanumeric characters are allowed')

class ShowRoom(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=50, null=True, blank=True, validators=[alphanumeric])
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    def __str__(self):
        if self.name:
            return self.name
        return f"Car {self.id}"