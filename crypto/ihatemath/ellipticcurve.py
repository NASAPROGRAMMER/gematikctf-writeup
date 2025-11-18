# ellipticcurve.py
# Simple elliptic curve implementation for CTF challenges

class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y

    def is_infinity(self):
        return self.x is None and self.y is None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        if self.is_infinity():
            return "Point(infinity)"
        return f"({self.x}, {self.y})"

    def __add__(self, Q):
        if self.is_infinity():
            return Q
        if Q.is_infinity():
            return self

        x1, y1 = self.x, self.y
        x2, y2 = Q.x, Q.y
        p = self.curve.p

        if x1 == x2 and (y1 + y2) % p == 0:
            # Point + inverse = infinity
            return Point(self.curve, None, None)

        if x1 == x2 and y1 == y2:
            # Point doubling
            s = (3 * x1 * x1 + self.curve.a) * pow(2 * y1, -1, p)
            s %= p
        else:
            # Standard addition
            s = (y2 - y1) * pow(x2 - x1, -1, p)
            s %= p

        xr = (s * s - x1 - x2) % p
        yr = (s * (x1 - xr) - y1) % p

        return Point(self.curve, xr, yr)

    def __mul__(self, n):
        # Scalar multiplication (double and add)
        result = Point(self.curve, None, None)  # infinity
        addend = self

        while n > 0:
            if n & 1:
                result = result + addend
            addend = addend + addend
            n >>= 1

        return result


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def __str__(self):
        return f"y = x**3 + {self.a}x + {self.b} % {self.p}"

    def is_on_curve(self, x, y):
        return (y * y - (x * x * x + self.a * x + self.b)) % self.p == 0

    def point(self, x):
        # Given x, compute y^2 = x^3 + ax + b mod p
        p = self.p
        rhs = (x * x * x + self.a * x + self.b) % p

        y = pow(rhs, (p + 1) // 4, p)  # p % 4 == 3 typical trick
        if (y * y) % p != rhs:
            return None

        return Point(self, x, y)
