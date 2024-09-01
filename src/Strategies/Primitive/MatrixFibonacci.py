from src.Strategies.FibonacciStrategy import FibonacciStrategy

class MatrixFibonacci(FibonacciStrategy):
    """
    Implements the matrix method for calculating Fibonacci numbers.

    This method uses the property that the nth Fibonacci number can be obtained
    from the nth power of a 2x2 matrix. It employs the fast exponentiation algorithm
    to compute the matrix power efficiently, reducing the time complexity to O(log n).
    """

    def execute(self, n):
        """Execute the matrix method to calculate the nth Fibonacci number."""
        return self.fibonacci_matrix(n)

    def fibonacci_matrix(self, n):
        """Calculate the nth Fibonacci number using matrix exponentiation."""
        F = [[1, 1], [1, 0]]  # Base matrix for Fibonacci sequence
        result = self.matrix_pow(F, n)
        return result[0][1]  # The nth Fibonacci number is in this position

    @staticmethod
    def matrix_mult(A, B):
        """
        Multiply two 2x2 matrices.

        This is a key operation in the matrix method, used in the exponentiation process.
        """
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def matrix_pow(self, mat, p):
        """
        Compute the pth power of a matrix using fast exponentiation.

        This method reduces the number of matrix multiplications from O(n) to O(log n),
        significantly improving the efficiency for large n.
        """
        result = [[1, 0], [0, 1]]  # Identity matrix
        while p > 0:
            if p & 1:  # If p is odd
                result = self.matrix_mult(result, mat)
            mat = self.matrix_mult(mat, mat)  # Square the matrix
            p >>= 1  # Divide p by 2
        return result
