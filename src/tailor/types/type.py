"""Tailor base type"""


class Type:
    def __init__(self, description=None):
        self._description = description

    @property
    def description(self):
        return self._description

    @property
    def type_name(self):
        return self.__class__.__name__.lower()
