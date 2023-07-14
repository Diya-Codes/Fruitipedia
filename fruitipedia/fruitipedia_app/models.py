from django.core.validators import MinLengthValidator
from fruitipedia.fruitipedia_app.validators import validate_starts_with_letter, validate_contains_letters_only
from django.db import models


class Profile(models.Model):
    """Model for the user profile"""
    first_name = models.CharField(blank=False,
                                  null=False,
                                  max_length=25,
                                  validators=[MinLengthValidator(2), validate_starts_with_letter])

    last_name = models.CharField(blank=False,
                                 null=False,
                                 max_length=35,
                                 validators=[MinLengthValidator(1), validate_starts_with_letter])

    email = models.EmailField(blank=False, null=False, max_length=40)

    password = models.CharField(blank=False,
                                null=False,
                                max_length=20,
                                validators=[MinLengthValidator(8)])

    image_url = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, default=18)

    def __str__(self):
        return f'{self.pk} {self.first_name} {self.last_name} {self.age}'


class Fruit(models.Model):
    """Model for the fruit"""
    name = models.CharField(blank=False,
                            null=False,
                            max_length=30,
                            validators=[MinLengthValidator(2), validate_contains_letters_only])

    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    nutrition = models.TextField(blank=True, null=True)