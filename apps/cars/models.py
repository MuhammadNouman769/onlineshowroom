
""" ============== IMPORTS =============== """
from contextlib import nullcontext
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError('Only alphanumeric characters are allowed')

""" ============== ShowRoom Models =============== """

class ShowRoom(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


""" ============== Cars Model =============== """

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
    showroom = models.ForeignKey(ShowRoom, related_name='cars', on_delete=models.CASCADE,default=1 )
    def __str__(self):
        if self.name:
            return self.name
        return f"Car {self.id}"


class Review(models.Model):
    car = models.ForeignKey(Cars,related_name='reviews' ,on_delete=models.CASCADE,null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " the rating of " + self.car.name + " :---- " + str(self.rating)





















