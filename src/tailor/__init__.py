"""Tailor package"""
from tailor.exceptions import UndefinedTypeError
from tailor.types import TYPES
from tailor.types.type import Type


def load(data_type: dict) -> Type:
    typ = data_type.pop('type', 'string')

    if typ not in TYPES:
        raise UndefinedTypeError("Undefined type '{0}'".format(typ))

    return TYPES[typ](**data_type)
