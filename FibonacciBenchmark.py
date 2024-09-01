import time
import json
import csv
import logging
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from tqdm import tqdm
from typing import List, Callable, Dict, Any

class FibonacciBenchmark:
    """
    A class for benchmarking Fibonacci calculation strategies.
    """

    def __init__(self, max_n: int, spread: int, timeout: float):
        """
        Initialize the FibonacciBenchmark.

        :param max_n: Maximum Fibonacci number to calculate.
        :param spread: Step size between Fibonacci numbers.
        :param timeout: Maximum execution time for each calculation.
        """
        self.max_n = max_n
        self.spread = spread
        self.timeout = timeout
        self.results: Dict[str, Dict[str, Any]] = {}

    def _timed_execution(self, func: Callable[[int], Any], n: int) -> float:
        """
        Execute the function with a timeout and return the execution time.

        :param func: Function to execute.
        :param n: Input parameter for the function.
        :return: Execution time in seconds.
        """
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self._measure_time, func, n)
            try:
                return future.result(timeout=self.timeout)
            except TimeoutError:
                raise

    @staticmethod
    def _measure_time(func: Callable[[int], Any], n: int) -> float:
        """
        Measure the execution time of a function.

        :param func: Function to measure.
        :param n: Input parameter for the function.
        :return: Execution time in seconds.
        """
        start_time = time.perf_counter()
        func(n)
        end_time = time.perf_counter()
        return end_time - start_time

    def _time_function(self, func: Callable[[int], Any], overall_pbar: tqdm) -> Dict[str, Any]:
        """
        Time the execution of a function for various input sizes.

        :param func: Function to time.
        :param overall_pbar: Progress bar for overall execution.
        :return: Dictionary containing timing results.
        """
        times = []
        n = 0

        while n < self.max_n:
            try:
                execution_time = self._timed_execution(func, n)
                times.append(execution_time)
            except TimeoutError:
                logging.warning(f"Execution timed out for n={n}")
                overall_pbar.update((self.max_n // self.spread + 1) - (n // self.spread))
                break
            except RecursionError:
                logging.warning(f"Recursion error for n={n}")
                overall_pbar.update((self.max_n // self.spread + 1) - (n // self.spread))
                break

            n += self.spread
            overall_pbar.update(1)

        return {
            'times': times,
            'average': sum(times) / len(times) if times else None,
            'min': min(times) if times else None,
            'max': max(times) if times else None
        }

    def _write_results_to_json(self, filename: str) -> None:
        """
        Write benchmark results to a JSON file.

        :param filename: Name of the output JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self.results, file, indent=2)

    def _write_results_to_csv(self, filename: str) -> None:
        """
        Write benchmark results to a CSV file.

        :param filename: Name of the output CSV file.
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['strategy', 'n', 'time'])
            for strategy, result in self.results.items():
                for n, time in enumerate(result['times']):
                    writer.writerow([strategy, n * self.spread, time])

    def run_benchmark(self, strategies: List[Any], csv_filename: str, json_filename: str) -> None:
        """
        Run the benchmark on given strategies and save results.

        :param strategies: List of strategy objects to benchmark.
        :param csv_filename: Name of the output CSV file.
        :param json_filename: Name of the output JSON file.
        """
        logging.info("Starting benchmark...")
        total_iterations = len(strategies) * (self.max_n // self.spread + 1)

        with tqdm(total=total_iterations, desc="Overall Progress", position=0) as overall_pbar:
            for strategy in strategies:
                strategy_name = strategy.__class__.__name__
                logging.info(f"Benchmarking {strategy_name}...")

                result = self._time_function(strategy.execute, overall_pbar)
                self.results[strategy_name] = result

                logging.info(f"{strategy_name} average time: {result['average']:.6f} seconds")

        if csv_filename:
            self._write_results_to_csv(csv_filename)
            logging.info(f"Results written to CSV: {csv_filename}")
        if json_filename:
            self._write_results_to_json(json_filename)
            logging.info(f"Results written to JSON: {json_filename}")

        logging.info("Benchmark completed.")

def run_fibonacci_benchmark(max_n: int, spread: int, timeout: float, strategies: List[Any],
                            csv_filename: str, json_filename: str) -> None:
    """
    Run a comprehensive Fibonacci benchmark.

    :param max_n: Maximum Fibonacci number to calculate.
    :param spread: Step size between Fibonacci numbers.
    :param timeout: Maximum execution time for each calculation.
    :param strategies: List of strategy objects to benchmark.
    :param csv_filename: Name of the output CSV file.
    :param json_filename: Name of the output JSON file.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    benchmark = FibonacciBenchmark(max_n=max_n, spread=spread, timeout=timeout)
    benchmark.run_benchmark(strategies, csv_filename, json_filename)

# Example usage:
if __name__ == "__main__":
    from src.Strategies.GMP.GMPDoublingFibonacci import GMPDoublingFibonacci
    from src.Strategies.GMP.GMPDoublingFibonacciOptimized import GMPDoublingFibonacciOptimized

    run_fibonacci_benchmark(
        max_n=10000000,
        spread=2000,
        timeout=1,
        strategies=[GMPDoublingFibonacciOptimized(), GMPDoublingFibonacci()],
        csv_filename='results.csv',
        json_filename='results.json'
    )