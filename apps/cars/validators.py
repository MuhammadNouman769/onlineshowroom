# apps/cars/validators.py

from django.core.exceptions import ValidationError

def alphanumeric(value):
    """
    Validator to ensure the field contains only alphanumeric characters.
    """
    if not value.isalnum():
        raise ValidationError('This field must be alphanumeric.')