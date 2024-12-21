from enum import Enum


def get_enum_member(enum_class, value) -> Enum:
    if not isinstance(enum_class, type(Enum)):
        raise ValueError("Enum class not provided, expected an `Enum` or subclass of `Enum` but got %s" % enum_class.__class__.__name__)

    for member in enum_class:
        if member.value == value or member.name == value:
            return member

    return None