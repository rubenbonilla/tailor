"""Tailor types module"""
from tailor.types.array import Array
from tailor.types.date import Date
from tailor.types.datetime import Datetime
from tailor.types.email import Email
from tailor.types.integer import Integer
from tailor.types.number import Number
from tailor.types.object import Object
from tailor.types.string import String
from tailor.types.time import Time
from tailor.types.url import Url


TYPES = {
    'array': Array,
    'date': Date,
    'datetime': Datetime,
    'email': Email,
    'integer': Integer,
    'number': Number,
    'object': Object,
    'string': String,
    'time': Time,
    'url': Url
}
