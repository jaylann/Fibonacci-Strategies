
from src.Strategies.FibonacciStrategy import FibonacciStrategy
import gmpy2

class GMPIterativeFibonacci(FibonacciStrategy):
    """
    Implements an iterative approach to calculate Fibonacci numbers using GMP.
    
    This class uses the GNU Multiple Precision Arithmetic Library (GMP) via the gmpy2 interface
    to handle arbitrarily large integers. GMP arithmetic is generally faster than python primitives.

    Note: Due to the overhead of GMP operations, this method might be slower for small Fibonacci numbers.
    However, it becomes significantly faster and more memory-efficient for large Fibonacci numbers.
    """

    def execute(self, n):
        """
        Execute the Fibonacci calculation for the given number using GMP.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            gmpy2.mpz: The nth Fibonacci number as a GMP integer.
        """
        return self.fib(n)

    def fib(self, n):
        """
        Calculate the nth Fibonacci number using an iterative approach with GMP.

        This method is similar to the standard iterative approach, but uses GMP integers.
        The use of GMP allows for efficient calculation of arbitrarily large Fibonacci numbers
        without the risk of integer overflow.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            gmpy2.mpz: The nth Fibonacci number as a GMP integer.
        """
        # Initialize a and b as GMP integers
        a, b = gmpy2.mpz(0), gmpy2.mpz(1)
        for _ in range(n):
            # Update a and b using GMP arithmetic operations
            # This is similar to the standard iterative approach, but uses GMP's
            # arbitrary-precision arithmetic for all calculations
            a, b = b, a + b
        return a  # After n iterations, a holds the nth Fibonacci number as a GMP integer