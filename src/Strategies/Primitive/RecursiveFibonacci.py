from src.Strategies.FibonacciStrategy import FibonacciStrategy


class RecursiveFibonacci(FibonacciStrategy):
    """
    A class that implements the recursive Fibonacci calculation strategy.

    This class uses a simple recursive approach to calculate Fibonacci numbers.
    While straightforward, this method is not optimized and has exponential time complexity,
    making it inefficient for large values of n.

    The recursive approach directly mirrors the mathematical definition of Fibonacci numbers:
    F(n) = F(n-1) + F(n-2), with base cases F(0) = 0 and F(1) = 1.
    """

    def execute(self, n):
        """
        Execute the Fibonacci calculation for a given number.

        Args:
            n (int): The position in the Fibonacci sequence to calculate.

        Returns:
            int: The Fibonacci number at position n.
        """
        return self.fib(n)

    def fib(self, n):
        """
        Recursively calculate the Fibonacci number at position n.

        This method directly implements the recursive definition of Fibonacci numbers.
        While intuitive, it's inefficient due to repeated calculations of the same values.

        Args:
            n (int): The position in the Fibonacci sequence to calculate.

        Returns:
            int: The Fibonacci number at position n.
        """
        # Base cases: F(0) = 0, F(1) = 1
        if n <= 1:
            return n

        # Recursive case: F(n) = F(n-1) + F(n-2)
        return self.fib(n-1) + self.fib(n-2)
