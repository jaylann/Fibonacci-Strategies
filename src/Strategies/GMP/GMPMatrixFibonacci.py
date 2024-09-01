from src.Strategies.FibonacciStrategy import FibonacciStrategy
import gmpy2

class GMPMatrixFibonacci(FibonacciStrategy):
    """
    Implements the matrix method for calculating Fibonacci numbers using GMP.

    This method is similar to MatrixFibonacci but uses GMP (GNU Multiple Precision
    Arithmetic Library) for arbitrary-precision arithmetic.

    Note: Due to the overhead of GMP operations, this method might be slower
    for small Fibonacci numbers but becomes significantly faster for large numbers.
    """

    def execute(self, n):
        """Execute the GMP matrix method to calculate the nth Fibonacci number."""
        return self.fibonacci_matrix(n)

    def fibonacci_matrix(self, n):
        """Calculate the nth Fibonacci number using GMP matrix exponentiation."""
        F = [[gmpy2.mpz(1), gmpy2.mpz(1)], [gmpy2.mpz(1), gmpy2.mpz(0)]]  # Base matrix
        result = self.matrix_pow(F, n)
        return result[0][1]  # The nth Fibonacci number

    @staticmethod
    def matrix_mult(A, B):
        """
        Multiply two 2x2 matrices using GMP.

        This operation benefits from GMP's arbitrary-precision arithmetic,
        allowing for exact results even with very large numbers.
        """
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def matrix_pow(self, mat, p):
        """
        Compute the pth power of a matrix using fast exponentiation and GMP.

        This method combines the efficiency of fast exponentiation with GMP's
        ability to handle arbitrarily large integers.
        """
        result = [[gmpy2.mpz(1), gmpy2.mpz(0)], [gmpy2.mpz(0), gmpy2.mpz(1)]]  # Identity matrix
        while p > 0:
            if p & 1:
                result = self.matrix_mult(result, mat)
            mat = self.matrix_mult(mat, mat)
            p >>= 1
        return result