# write a program to perform property exception handling
class Property:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise ValueError("Value must be an integer.")
        if new_value < 0:
            raise ValueError("Value must be non-negative.")
        self._value = new_value