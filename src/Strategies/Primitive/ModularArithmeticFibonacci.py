from src.Strategies.FibonacciStrategy import FibonacciStrategy


class ModularArithmeticFibonacci(FibonacciStrategy):
    """
    Implements the modular arithmetic method for calculating Fibonacci numbers.

    This method uses a more optimized version of the matrix method, reducing
    the number of operations and memory usage by working directly with the
    matrix elements instead of full matrices.
    """

    def execute(self, n):
        """Execute the modular arithmetic method to calculate the nth Fibonacci number."""
        return self.mat_fib(n)

    def mat_fib(self, n):
        """
        Calculate the nth Fibonacci number using modular arithmetic.

        This method represents the matrix multiplication and exponentiation
        operations using individual variables instead of full matrices,
        reducing memory usage and improving cache efficiency.
        """
        a, b, c, d = 0, 1, 1, 1  # Initial matrix [[0, 1], [1, 1]]
        x, z = 0, 1  # Initial vector [0, 1]
        while n:
            n, r = divmod(n, 2)
            if r:  # If n is odd
                x, z = a*x + b*z, c*x + d*z  # Multiply current matrix with vector
            if n:  # If n is not zero
                # Square the current matrix
                a, b, c, d = a*a + b*c, b*(a + d), c*(a + d), c*b + d*d
        return x  # x holds the nth Fibonacci number
