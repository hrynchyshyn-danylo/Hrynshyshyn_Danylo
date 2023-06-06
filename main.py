class DataType:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class Numeric(DataType):
    def __init__(self, value):
        super().__init__(value)

    def add(self, other):
        pass

class Integer(Numeric):
    def __init__(self, value):
        super().__init__(value)

    def is_even(self):
        pass

class Float(Numeric):
    def __init__(self, value):
        super().__init__(value)

    def is_integer(self):
        pass

class String(DataType):
    def __init__(self, value):
        super().__init__(value)

    def length(self):
        pass

class Boolean(DataType):
    def __init__(self, value):
        super().__init__(value)

    def negate(self):
        pass

class List(DataType):
    def __init__(self, value):
        super().__init__(value)

    def append(self, item):
        pass

class Dictionary(DataType):
    def __init__(self, value):
        super().__init__(value)

    def get_keys(self):
        pass
