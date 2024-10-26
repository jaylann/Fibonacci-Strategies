import gmpy2

from src.Strategies.FibonacciStrategy import FibonacciStrategy


class GMPImprovedMatrixFibonnaci(FibonacciStrategy):
    """
    Implements the modular arithmetic method for calculating Fibonacci numbers using GMP.

    This method combines the optimizations of ImprovedMatrixFibonnaci with GMP's
    arbitrary-precision arithmetic. It provides the best performance for calculating
    extremely large Fibonacci numbers.

    Note: Like GMPMatrixFibonacci, this method may be slower for small numbers due to
    GMP overhead, but it excels for large Fibonacci calculations.
    """

    def execute(self, n):
        """Execute the GMP modular arithmetic method to calculate the nth Fibonacci number."""
        return self.mat_fib_mpz(n)

    def mat_fib_mpz(self, n):
        """
        Calculate the nth Fibonacci number using GMP modular arithmetic.

        This method uses individual GMP variables to represent matrix elements,
        combining the memory efficiency of ModularArithmeticFibonacci with GMP's
        ability to handle arbitrarily large integers.
        """
        a = gmpy2.mpz(0)
        b = gmpy2.mpz(1)
        c = gmpy2.mpz(1)
        d = gmpy2.mpz(1)
        x = gmpy2.mpz(0)
        z = gmpy2.mpz(1)

        while n > 0:
            n, r = divmod(n, 2)
            if r:  # If n is odd
                x, z = a*x + b*z, c*x + d*z  # Multiply current matrix with vector
            if n:  # If n is not zero
                # Square the current matrix
                a, b, c, d = a*a + b*c, b*(a + d), c*(a + d), c*b + d*d

        return x  # x holds the nth Fibonacci number