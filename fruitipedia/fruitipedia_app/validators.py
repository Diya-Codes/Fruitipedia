from django.core import exceptions


def validate_starts_with_letter(name):
    """Validator function for checking if the name starts with a letter"""
    if not name[0].isalpha():
        raise exceptions.ValidationError('Your name must start with a letter!')


def validate_contains_letters_only(name):
    """Validator function for checking if the name contains only letters"""
    if not name.isalpha():
        raise exceptions.ValidationError('Fruit name should contain only letters!')
