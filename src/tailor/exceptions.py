"""Tailor package exceptions"""


class TailorError(Exception):
    pass


class TailorTypeError(TailorError):
    pass


class UndefinedTypeError(TailorTypeError):
    pass
