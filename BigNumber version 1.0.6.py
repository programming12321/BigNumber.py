# added hyperoperations
from math import *

class BigNumber:

    def __init__(self, mantissa=0, exponent=0, layer=0, pentate=0, hexate=0, hyper=0):
        self.m = float(mantissa)
        self.e = float(exponent)
        self.l = int(layer)
        self.pe = int(pentate)
        self.he = int(hexate)
        self.hy = int(hyper)

        self.normalize()

    def normalize(self):

        if self.m == 0:
            self.e = 0
            self.l = 0
            self.pe = 0
            self.he = 0
            self.hy = 0
            return

        sign = -1 if self.m < 0 else 1

        self.m = abs(self.m)

        while self.m >= 10:
            self.m /= 10
            self.e += 1

        while self.m < 1:
            self.m *= 10
            self.e -= 1

        while self.e >= 1e308:
            self.e = log10(self.e)
            self.l += 1

        while self.l >= 1e308:
            self.l = log10(self.l)
            self.pe += 1

        while self.pe >= 1e308:
            self.pe = log10(self.pe)
            self.he += 1

        while self.he >= 1e308:
            self.he = log10(self.he)
            self.hy += 1

        self.m *= sign

    def add(self, other):

        if self.hy > other.hy:
            return self

        if other.hy > self.hy:
            return other

        if self.he > other.he:
            return self

        if other.he > self.he:
            return other

        if self.pe > other.pe:
            return self

        if other.pe > self.pe:
            return other

        if self.l > other.l:
            return self

        if other.l > self.l:
            return other

        if self.l > 0:

            if abs(self.e - other.e) > 15:
                return self if self.e > other.e else other

            return BigNumber(
                1,
                max(self.e, other.e),
                self.l,
                self.pe,
                self.he,
                self.hy
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

        return BigNumber(m, e, self.l, self.pe, self.he, self.hy)

    def sub(self, other):

        if self.hy > other.hy:
            return self

        if other.hy > self.hy:
            return BigNumber.ZERO

        if self.he > other.he:
            return self

        if other.he > self.he:
            return BigNumber.ZERO

        if self.pe > other.pe:
            return self

        if other.pe > self.pe:
            return BigNumber.ZERO

        if self.l > other.l:
            return self

        if other.l > self.l:
            return BigNumber.ZERO

        if self.l > 0:

            if abs(self.e - other.e) > 15:
                return self if self.e > other.e else BigNumber.ZERO

            if self.e >= other.e:
                return BigNumber(
                    1,
                    self.e,
                    self.l,
                    self.pe,
                    self.he,
                    self.hy
                )

            return BigNumber.ZERO

        if abs(self.e - other.e) > 15:
            return self if self.e > other.e else BigNumber.ZERO

        if self.e > other.e:

            diff = self.e - other.e

            m = self.m - other.m / (10 ** diff)
            e = self.e

        else:

            diff = other.e - self.e

            m = self.m / (10 ** diff) - other.m
            e = other.e

        return BigNumber(m, e, self.l, self.pe, self.he, self.hy)

    def mul(self, other):

        if self.hy > other.hy:
            return self

        if other.hy > self.hy:
            return other

        if self.he > other.he:
            return self

        if other.he > self.he:
            return other

        if self.pe > other.pe:
            return self

        if other.pe > self.pe:
            return other

        if self.l == 0 and other.l == 0:

            return BigNumber(
                self.m * other.m,
                self.e + other.e
            )

        if self.l > other.l:
            return self

        if other.l > self.l:
            return other

        return BigNumber(
            1,
            self.e + other.e,
            self.l,
            self.pe,
            self.he,
            self.hy
        )

    def div(self, other):

        if other.m == 0:
            return BigNumber.INFINITY

        if self.hy > other.hy:
            return self

        if other.hy > self.hy:
            return BigNumber.ZERO

        if self.he > other.he:
            return self

        if other.he > self.he:
            return BigNumber.ZERO

        if self.pe > other.pe:
            return self

        if other.pe > self.pe:
            return BigNumber.ZERO

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
            self.l,
            self.pe,
            self.he,
            self.hy
        )

    def power(self, other):

        if isinstance(other, BigNumber):
            other = other.tofloat()

        if self.hy > 0:

            return BigNumber(
                1,
                self.e,
                self.l,
                self.pe,
                self.he,
                self.hy + 1
            )

        if self.he > 0:

            return BigNumber(
                1,
                self.e,
                self.l,
                self.pe,
                self.he + 1,
                self.hy
            )

        if self.pe > 0:

            return BigNumber(
                1,
                self.e,
                self.l,
                self.pe + 1,
                self.he,
                self.hy
            )

        if self.l > 0:

            return BigNumber(
                1,
                self.e * other,
                self.l + 1,
                self.pe,
                self.he,
                self.hy
            )

        total_log = (log10(self.m) + self.e) * other

        return BigNumber(
            1,
            total_log,
            1,
            0,
            0,
            0
        )

    def tofloat(self):

        if self.l > 0 or self.pe > 0 or self.he > 0 or self.hy > 0:
            return float("inf")

        if self.e >= 308:
            return float("inf")

        return self.m * (10 ** self.e)

    def tointeger(self):

        if self.e >= 20:
            return str(self.m) + "*10^" + str(self.e)

        return round(self.m * (10 ** self.e))

    def tostring(self):

        if self.hy > 0:
            return "10{" + str(self.hy) + "}" + str(round(self.he, 3)) + ""

        if self.he > 0:
            return "H" + str(self.he) + "(" + str(round(self.pe, 3)) + ")"

        if self.pe > 0:
            return "G" + str(self.pe) + "(" + str(round(self.l, 3)) + ")"

        if self.l == 0:
            return f"{self.m:.3f}e{int(self.e)}"

        if self.l < 10:
            return "e" * self.l + str(round(self.e, 3))

        return "F" + str(self.l) + "(" + str(round(self.e, 3)) + ")"

    def greaterThan(self, other):

        if self.hy != other.hy:
            return self.hy > other.hy

        if self.he != other.he:
            return self.he > other.he

        if self.pe != other.pe:
            return self.pe > other.pe

        if self.l != other.l:
            return self.l > other.l

        if self.e != other.e:
            return self.e > other.e

        return self.m > other.m

    def lessThan(self, other):

        if self.hy != other.hy:
            return self.hy < other.hy

        if self.he != other.he:
            return self.he < other.he

        if self.pe != other.pe:
            return self.pe < other.pe

        if self.l != other.l:
            return self.l < other.l

        if self.e != other.e:
            return self.e < other.e

        return self.m < other.m

    def greaterThanOrEqual(self, other):
        return not self.lessThan(other)

    def lessThanOrEqual(self, other):
        return not self.greaterThan(other)

    def equalTo(self, other):

        return (
            self.m == other.m and
            self.e == other.e and
            self.l == other.l and
            self.pe == other.pe and
            self.he == other.he and
            self.hy == other.hy
        )

    def isinf(self):
        return self.hy > 1000000

    def rounded(self):

        if self.e >= 20 or self.l > 0 or self.pe > 0 or self.he > 0 or self.hy > 0:
            return self.tostring()

        return round(self.m * (10 ** self.e))

    def absValue(self):
        return BigNumber(abs(self.m), self.e, self.l, self.pe, self.he, self.hy)

BigNumber.PI = BigNumber(3.14159265359, 0)
BigNumber.E = BigNumber(2.71828182846, 0)
BigNumber.ZERO = BigNumber(0, 0)
BigNumber.ONE = BigNumber(1, 0)
BigNumber.INFINITY = BigNumber(1, 308, 1)
BigNumber.NEG_INF = BigNumber(-1, 308, 1)
