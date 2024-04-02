class EuclideanAlgorithm:
    def gcd(self, a, b):
        """finds the Greatest common divisor"""
        if a == 0:
            # GCD(0, b) = b
            return b
        elif b == 0:
            # GCD(a, 0) = a
            return a
        else:
            # a = b * quotient + remainder
            remainder = a % b
            # call the function again
            return self.gcd(b, remainder)