from src.Strategies.FibonacciStrategy import FibonacciStrategy
class IterativeFibonacci(FibonacciStrategy):
    """
    Implements an iterative approach to calculate Fibonacci numbers.

    This class uses a simple iterative method to compute Fibonacci numbers.
    It's more efficient than the recursive approach, especially for larger numbers,
    as it avoids the overhead of function calls and potential stack overflow issues.
    """

    def execute(self, n):
        """
        Execute the Fibonacci calculation for the given number.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.
        """
        return self.fib(n)

    def fib(self, n):
        """
        Calculate the nth Fibonacci number using an iterative approach.

        This method uses two variables to keep track of the previous two Fibonacci numbers,
        updating them in each iteration. This approach has a time complexity of O(n) and
        a space complexity of O(1), making it efficient for most use cases.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.
        """
        a, b = 0, 1  # Initialize the first two Fibonacci numbers
        for _ in range(n):
            # Update a and b simultaneously:
            # a becomes the previous b (the n-1 Fibonacci number)
            # b becomes the sum of previous a and b (the nth Fibonacci number)
            a, b = b, a + b
        return a  # After n iterations, a holds the nth Fibonacci number
