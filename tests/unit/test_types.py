"""Test types."""


def test_default_type():
    from tailor import load
    assert load({}).type_name == 'string'


def test_undefined_type():
    from pytest import raises

    from tailor.exceptions import TailorError
    from tailor.exceptions import TailorTypeError
    from tailor.exceptions import UndefinedTypeError
    from tailor import load

    typ = 'undefined'
    msg = "Undefined type '{0}'".format(typ)

    with raises(UndefinedTypeError, message=msg) as exc_info:
        load({'type': typ})

    assert issubclass(exc_info.type, TailorTypeError)
    assert issubclass(exc_info.type, TailorError)


def test_supported_types():
    from tailor import load
    from tailor.types.type import Type

    types = [
        'array', 'date', 'datetime', 'email',
        'integer', 'number', 'object', 'string',
        'time', 'url'
    ]

    for typ in types:
        assert isinstance(load({'type': typ}), Type)


def test_description_type():
    from tailor import load
    txt = 'Description type'
    assert load({'description': txt}).description == txt
