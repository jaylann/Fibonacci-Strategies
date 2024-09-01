import gmpy2

from src.Strategies.FibonacciStrategy import FibonacciStrategy


class GMPDoublingFibonacci(FibonacciStrategy):
    """
    Implements the doubling method for Fibonacci calculation using GMP (GNU Multiple Precision Arithmetic Library).

    The doubling method is based on the matrix form of Fibonacci sequence:
    [F(n+1) F(n)  ] = [1 1]^n
    [F(n)   F(n-1)]   [1 0]

    It uses the fact that we can square this matrix to quickly compute higher Fibonacci numbers,
    effectively doubling the index with each operation.
    """

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
        def _fibonacci_doubling_mpz(n):
            if n == 0:
                return (gmpy2.mpz(0), gmpy2.mpz(1))
            else:
                # Recursively compute F(n/2) and F(n/2 + 1)
                a, b = _fibonacci_doubling_mpz(n >> 1)  # n >> 1 is equivalent to n // 2
                c = a * (gmpy2.mpz(2) * b - a)  # Compute F(n) using the doubling formula
                d = a * a + b * b  # Compute F(n+1)
                if n & 1:  # If n is odd
                    return (d, c + d)  # Return F(n+1) and F(n+2)
                else:
                    return (c, d)  # Return F(n) and F(n+1)

        # Return the first element of the tuple, which is F(n)
        return _fibonacci_doubling_mpz(n)[0]
