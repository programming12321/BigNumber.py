class BigNumber:
    def __init__(self, mantissa=0, exponent=0):
        self.m = float(mantissa)
        self.e = int(exponent)
        self.normalize()

    # DON'T DELETE IT
    def normalize(self):
        while self.m >= 10:
            self.m /= 10
            self.e += 1

        while self.m < 1 and self.m != 0:
            self.m *= 10
            self.e -= 1

    def add(self, other):
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
        return BigNumber(self.m * other.m, self.e + other.e)
    
    def div(self, other):
        return BigNumber(self.m / other.m, self.e - other.e)
    
    # LIMIT is 10 ^ 20
    def tofloat(self):

        if self.e >= 20:
            return float("inf")

        return self.m * (10 ** self.e)
    
    def power(self, other):
        if isinstance(other, BigNumber):
            p = other.tofloat()
        else:
            p = float(other)

        import math

        total_log = (math.log10(self.m) + self.e) * p

        new_e = int(math.floor(total_log))
        new_m = 10 ** (total_log - new_e)

        return BigNumber(new_m, new_e)
    
    # IMPORTANT: limit is 10 ^ 1000 or 10 ^ 5000
    def tointeger(self):
        if self.e >= 20:
            return str(self.m) + "*10^" + str(self.e)

        return round(self.m * (10 ** self.e))

    # IMPORTANT: limit is 10 ^ (10 ^ 308)
    def tostring(self):
        return f"{self.m:.3f}e{self.e}"
    
    def greaterThan(self, other):
        if self.e != other.e:
            return self.e > other.e
        return self.m > other.m
    
    def lessThan(self, other):
        if self.e != other.e:
            return self.e < other.e
        return self.m < other.m
    
    def greaterThanOrEqual(self, other):
        if self.e != other.e:
            return self.e >= other.e
        return self.m >= other.m
    
    def lessThanOrEqual(self, other):
        if self.e != other.e:
            return self.e <= other.e
        return self.m <= other.m
    
    def equalTo(self, other):
        if self.e != other.e:
            return self.e == other.e
        return self.m == other.m
    
    def isinf(self):
        return self.e >= 100000000
    
    def rounded(self):
        if self.e >= 20:
            return self.tostring()

        return round(self.m * (10 ** self.e))
    
    def abs(self):
        return BigNumber(abs(self.m), self.e)
    
BigNumber.PI = BigNumber(3.14159265359, 0)
BigNumber.E = BigNumber(2.71828182846, 0)
BigNumber.ZERO = BigNumber(0, 0)
BigNumber.ONE = BigNumber(1, 0)
