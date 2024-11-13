class Rectangle:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def area(self):
        return self.a * self.b


class Square(Rectangle):

    # Overriding the setters to maintain the square property

    def __init__(self, a, b=None):
        super().__init__(a, a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a, self._b = value, value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._a, self._b = value, value


def check_area(shape, a, b):
    shape.a = a
    shape.b = b
    return shape.area() == a * b


if __name__ == "__main__":
    print("rectangle")
    r1 = Rectangle(1, 2)
    print(r1.a, r1.b)  # 1, 2
    r1.a = 10  # 10, 2
    print(r1.a, r1.b)

    print("square")
    s1 = Square(2)
    print(s1.a, s1.b)  # 2, 2
    s1.a = 10
    print(s1.a, s1.b)  # 10, 10
    s1.b = 20
    print(s1.a, s1.b)  # 20, 20

    r = Rectangle(1, 1)
    s = Square(1)
    print(check_area(r, 5, 6))
    print(check_area(s, 5, 6))
