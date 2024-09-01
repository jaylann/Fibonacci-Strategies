from src.Strategies.FibonacciStrategy import FibonacciStrategy


class DoublingFibonacci(FibonacciStrategy):
    def execute(self, n):
        return self.fibonacci_doubling(n)

    def fibonacci_doubling(self, n):
        def _fibonacci_doubling(n):
            if n == 0:
                return (0, 1)
            else:
                a, b = _fibonacci_doubling(n >> 1)
                c = a * (2 * b - a)
                d = a * a + b * b
                if n & 1:
                    return (d, c + d)
                else:
                    return (c, d)

        return _fibonacci_doubling(n)[0]