# added tetration at version 1.0.1
# bug fixes at version 1.0.2
from math import *
class BigNumber:

    def __init__(self, mantissa=0, exponent=0, layer=0):
        self.m = float(mantissa)
        self.e = float(exponent)
        self.l = int(layer)

        self.normalize()

    def normalize(self):
        if self.m == 0:
            self.e = 0
            self.l = 0
            return

        sign = -1 if self.m < 0 else 1

        self.m = abs(self.m)

        if self.l == 0:

            while self.m >= 10:
                self.m /= 10
                self.e += 1

            while self.m < 1:
                self.m *= 10
                self.e -= 1

            if self.e >= 1e308:
                self.e = log10(self.e)
                self.m = 1
                self.l = 1

        else:

            self.m = 1

            while self.e >= 1e308:
                self.e = log10(self.e)
                self.l += 1

        self.m *= sign

    def add(self, other):
        if self.l > other.l:
            return self

        if other.l > self.l:
            return other

        if self.l > 0:

            if abs(self.e - other.e) > 15:
                return self if self.e > other.e else other

            if self.e > other.e:
                return BigNumber(
                    1,
                    self.e,
                    self.l
                )

            return BigNumber(
                1,
                other.e,
                other.l
            )

        if abs(self.e - other.e) > 15:
            return self if self.e > other.e else other

        if self.e > other.e:
            diff = self.e - other.e

            m = self.m + other.m / (10 ** diff)
            e = self.e

        else:
            diff = other.e - self.e

            m = self.m / (10 ** diff) + other.m
            e = other.e

        return BigNumber(m, e)
    def sub(self, other):
        if self.l > other.l:
            return self

        if other.l > self.l:
            return BigNumber.ZERO

        if self.l > 0:

            if abs(self.e - other.e) > 15:
                return self if self.e > other.e else BigNumber.ZERO

            if self.e > other.e:
                return BigNumber(
                    1,
                    self.e,
                    self.l
                )

            return BigNumber.ZERO

        if abs(self.e - other.e) > 15:
            return self if self.e > other.e else other

        if self.e > other.e:

            diff = self.e - other.e

            m = self.m - other.m / (10 ** diff)
            e = self.e

        else:

            diff = other.e - self.e

            m = self.m / (10 ** diff) - other.m
            e = other.e

        return BigNumber(m, e)

    def mul(self, other):
        if self.l == 0 and other.l == 0:
            return BigNumber(self.m * other.m, self.e + other.e)
        else:
            if self.l > 0 or other.l > 0:
                if self.l > other.l:
                    return self

                if other.l > self.l:
                    return other

                return BigNumber(1, self.e + other.e, self.l)
    
    def div(self, other):
        if self.l == 0 and other.l == 0:
            return BigNumber(
                self.m / other.m,
                self.e - other.e
            )

        if self.l > other.l:
            return self

        if other.l > self.l:
            return BigNumber.ZERO

        return BigNumber(
            1,
            self.e - other.e,
            self.l
        )
    
    # LIMIT is 10 ^ 20
    def tofloat(self):
        if self.l > 0:
            return float("inf")

        if self.e >= 308:
            return float("inf")

        return self.m * (10 ** self.e)
    
    def power(self, other):
        if isinstance(other, BigNumber):
            other = other.tofloat()

        if self.l == 0:

            total_log = (log10(self.m) + self.e) * other

            return BigNumber(1, total_log, 1)

        return BigNumber(1, self.e * other, self.l + 1)
    
    # IMPORTANT: limit is 10 ^ 1000 or 10 ^ 5000
    def tointeger(self):
        if self.e >= 20:
            return str(self.m) + "*10^" + str(self.e)

        return round(self.m * (10 ** self.e))

    # IMPORTANT: limit is 10 ^^ 10 ^ 308 (tetration is "^^")
    def tostring(self):
        if self.l == 0:
            return f"{self.m:.3f}e{int(self.e)}"

        if self.l < 10:
            return "e" * self.l + str(round(self.e, 3))

        return f"F{self.l}({round(self.e, 3)})"
    
    def greaterThan(self, other):
        if self.l != other.l:
            return self.l > other.l

        if self.e != other.e:
            return self.e > other.e

        return self.m > other.m
    
    def lessThan(self, other):
        if self.l != other.l:
            return self.l < other.l
        if self.e != other.e:
            return self.e < other.e
        return self.m < other.m
    
    def greaterThanOrEqual(self, other):
        if self.l != other.l:
            return self.l >= other.l
        if self.e != other.e:
            return self.e >= other.e
        return self.m >= other.m
    
    def lessThanOrEqual(self, other):
        if self.l != other.l:
            return self.l <= other.l
        if self.e != other.e:
            return self.e <= other.e
        return self.m <= other.m
    
    def equalTo(self, other):
        if self.l != other.l:
            return self.e == other.e
        if self.e != other.e:
            return self.e == other.e
        return self.m == other.m
    
    def isinf(self):
        return self.e >= 100000000
    
    def rounded(self):
        if self.e >= 20:
            return self.tostring()

        return round(self.m * (10 ** self.e))
    
    def absValue(self):
        return BigNumber(abs(self.m), self.e)
    
BigNumber.PI = BigNumber(3.14159265359, 0)
BigNumber.E = BigNumber(2.71828182846, 0)
BigNumber.ZERO = BigNumber(0, 0)
BigNumber.ONE = BigNumber(1, 0)
BigNumber.INFINITY = BigNumber(1, 1, 1e308)
