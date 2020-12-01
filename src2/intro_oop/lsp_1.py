class MutableRectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._get_a()

    @a.setter
    def a(self, a):
        self._set_a(a)

    @property
    def b(self):
        return self._get_b()

    @b.setter
    def b(self, b):
        self._set_b(b)

    def _get_a(self):
        return self._a

    def _set_a(self, a):
        self._a = a

    def _get_b(self):
        return self._b

    def _set_b(self, b):
        self._b = b


class MutableSquare(MutableRectangle):
    def __init__(self, a, b=None):
        self._a = a
        self._b = a

    def _set_a(self, a):
        self._a = a
        self._b = a

    def _set_b(self, b):
        self._a = b
        self._b = b


def f(s):
    s.a = 10
    s.b = 3
    print(s.a * s.b == 30)


s1 = MutableSquare(2, 5)
s2 = MutableRectangle(1, 1)
print(s1.a, s1.b)
s1.a = 10
print(s1.a, s1.b)

print('---')

f(s1)
f(s2)
