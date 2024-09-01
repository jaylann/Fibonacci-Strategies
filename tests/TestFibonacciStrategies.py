import unittest
import os
from typing import List
from src.Strategies import FibonacciStrategy
from src.Strategies.Primitive.IterativeFibonacci import IterativeFibonacci
from src.Strategies.GMP.GMPIterativeFibonacci import GMPIterativeFibonacci
from src.Strategies.Primitive.MatrixFibonacci import MatrixFibonacci
from src.Strategies.GMP.GMPMatrixFibonacci import GMPMatrixFibonacci
from src.Strategies.GMP.GMPDoublingFibonacci import GMPDoublingFibonacci
from src.Strategies.Primitive.DoublingFibonacci import DoublingFibonacci
from src.Strategies.GMP.GMPDoublingFibonacciOptimized import GMPDoublingFibonacciOptimized
from src.Strategies.Primitive.ModularArithmeticFibonacci import ModularArithmeticFibonacci
from src.Strategies.GMP.GMPModularArithmeticFibonacci import GMPModularArithmeticFibonacci

# Configuration
MAX_FIB_NUMBER = 10000  # Adjust this to change the number of Fibonacci numbers to compare
STORAGE_FILE = "./storage/tests/fib_nums.txt"

def load_or_generate_fibonacci_sequence(max_n: int) -> List[int]:
    """
    Loads Fibonacci sequence from file or generates it if file doesn't exist or is incomplete.

    Args:
        max_n (int): The maximum number of Fibonacci numbers to load/generate.

    Returns:
        List[int]: List of Fibonacci numbers.
    """
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as f:
            sequence = [int(num) for num in f.read().strip().split(',')]
        if len(sequence) >= max_n:
            return sequence[:max_n]

    # Generate sequence if file doesn't exist or is incomplete
    itFib = IterativeFibonacci()
    sequence = [itFib.execute(n) for n in range(max_n)]

    # Ensure directory exists
    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)

    # Save sequence to file
    with open(STORAGE_FILE, 'w') as f:
        f.write(','.join(map(str, sequence)))

    return sequence

def verify_fibonacci_strategy(strategy: FibonacciStrategy, reference_sequence: List[int]) -> bool:
    """
    Verifies the validity of a Fibonacci strategy based on the reference sequence.

    Args:
        strategy (FibonacciStrategy): The strategy to verify.
        reference_sequence (List[int]): The reference Fibonacci sequence.

    Returns:
        bool: True if the strategy is valid, False otherwise.
    """
    for i, expected in enumerate(reference_sequence):
        if strategy.execute(i) != expected:
            return False
    return True

class TestFibonacciStrategies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reference_sequence = load_or_generate_fibonacci_sequence(MAX_FIB_NUMBER)
        cls.strategies = [
            MatrixFibonacci(),
            GMPDoublingFibonacci(),
            DoublingFibonacci(),
            GMPDoublingFibonacciOptimized(),
            ModularArithmeticFibonacci(),
            GMPModularArithmeticFibonacci(),
            GMPMatrixFibonacci(),
            GMPIterativeFibonacci(),
        ]

    def test_fibonacci_strategies(self):
        """
        Tests the validity of all Fibonacci strategies.
        """
        for idx, strategy in enumerate(self.strategies):
            with self.subTest(f"Testing strategy {type(strategy).__name__}"):
                self.assertTrue(
                    verify_fibonacci_strategy(strategy, self.reference_sequence),
                    f"Strategy {type(strategy).__name__} failed Fibonacci verification"
                )
                print(f"Strategy {type(strategy).__name__} passed Fibonacci verification")

if __name__ == "__main__":
    unittest.main()