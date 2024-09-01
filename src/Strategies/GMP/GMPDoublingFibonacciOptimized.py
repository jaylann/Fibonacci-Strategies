from src.Strategies.FibonacciStrategy import FibonacciStrategy
import gmpy2

class GMPDoublingFibonacciOptimized(FibonacciStrategy):
    """
    Optimized version of the doubling method for Fibonacci calculation using GMP.

    This version improves upon the original by:
    1. Pre-computing commonly used GMP integers.
    2. Eliminating recursion to reduce function call overhead.
    3. Using bit manipulation for faster operations.
    """

    def __init__(self):
        super().__init__()
        # Pre-compute commonly used GMP integers for efficiency
        self.mpz_0 = gmpy2.mpz(0)
        self.mpz_1 = gmpy2.mpz(1)
        self.mpz_2 = gmpy2.mpz(2)

    def execute(self, n):
        """Execute the Fibonacci calculation for the given index."""
        return self.fibonacci_doubling_mpz(n)

    def fibonacci_doubling_mpz(self, n):
        """
        Calculate the nth Fibonacci number using the doubling method and GMP.

        Args:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            gmpy2.mpz: The nth Fibonacci number as a GMP integer.
        """
        # Base cases
        if n == 0:
            return self.mpz_0
        elif n == 1:
            return self.mpz_1

        a, b = self.mpz_0, self.mpz_1
        # Find the position of the highest set bit in n
        k = n.bit_length() - 1

        # Iterate through the bits of n from left to right
        for i in range(k, -1, -1):
            # Calculate F(2k) using the formula: F(2k) = F(k) * [2*F(k+1) - F(k)]
            c = a * ((self.mpz_2 * b) - a)
            # Calculate F(2k+1) using the formula: F(2k+1) = F(k+1)^2 + F(k)^2
            d = a * a + b * b

            # If the current bit is set, shift to the next odd Fibonacci number
            # Otherwise, shift to the next even Fibonacci number
            if (n >> i) & 1:
                a, b = d, c + d
            else:
                a, b = c, d

        # The final value of 'a' is the nth Fibonacci number
        return a