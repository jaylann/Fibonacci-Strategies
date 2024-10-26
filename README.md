# Fibonacci Benchmarking Suite

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A comprehensive benchmarking suite for evaluating and visualizing different Fibonacci number calculation strategies. This project allows you to compare the performance of various algorithms, generate detailed reports, and visualize the results with customizable plots.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Running the Benchmark](#running-the-benchmark)
    - [Visualizing Results](#visualizing-results)
- [Project Structure](#project-structure)
- [Supported Strategies](#supported-strategies)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Benchmark Multiple Strategies**: Easily add and benchmark different Fibonacci calculation algorithms.
- **Timeout Handling**: Set execution timeouts to prevent long-running calculations.
- **Progress Tracking**: Monitor the benchmarking process with progress bars.
- **Result Exporting**: Export benchmark results to CSV and JSON formats.
- **Data Visualization**: Generate high-quality plots to compare strategy performances.
- **Logging**: Detailed logging for monitoring and debugging.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jaylann/Fibonacci-Framework.git
   cd fibonacci-benchmark
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Benchmark

To execute the benchmark with your desired strategies:

1. **Import Your Strategies**

   Ensure that your Fibonacci strategies are implemented as classes with an `execute` method that takes an integer `n` and returns the nth Fibonacci number.

   ```python
   from src.Strategies.Primitive.RecursiveFibonacci import RecursiveFibonacci
   from src.Strategies.GMP.GMPDoublingFibonacci import GMPDoublingFibonacci
   from src.Strategies.GMP.GMPDoublingFibonacciOptimized import GMPDoublingFibonacciOptimized
   # And so on
   ```

   2. **Run the Benchmark**

      You can run the benchmark by executing the `fibonacci_benchmark.py` script or using the provided `run_fibonacci_benchmark` function.

      ```bash
      python FibonacciBenchmark.py
      ```

      Alternatively, customize the parameters directly in the script:

      ```python
      if __name__ == "__main__":
          run_fibonacci_benchmark(
              max_n=50001,
              spread=1,
              timeout=60,
              strategies=[RecursiveFibonacci(), IterativeFibonacci(), MatrixFibonacci(), ImprovedMatrixFibonnaci(), DoublingFibonacci(), GMPIterativeFibonacci(), GMPMatrixFibonacci(), GMPImprovedMatrixFibonnaci(), GMPDoublingFibonacci(), GMPImprovedMatrixFibonnaci()],
              csv_filename='data.csv',
              json_filename='data.json'
          )

      ```

      **Parameters:**

       - `max_n`: Maximum Fibonacci number to calculate.
       - `spread`: Step size between Fibonacci numbers.
       - `timeout`: Maximum execution time (in seconds) for each calculation.
       - `strategies`: List of strategy instances to benchmark.
       - `csv_filename`: Output CSV file name for results.
       - `json_filename`: Output JSON file name for results.

### Visualizing Results

After running the benchmark, you can visualize the results using the `BenchmarkVisualizer` class.

1. **Visualize from CSV**

   ```python
   from BenchmarkVisualizer import BenchmarkVisualizer

   visualizer = BenchmarkVisualizer('benchmark_results.csv', 'benchmark_plot_from_csv.png')
   visualizer.visualize()
   ```

2. **Visualize from JSON**

   ```python
   visualizer = BenchmarkVisualizer('benchmark_results.json', 'benchmark_plot_from_json.png')
   visualizer.visualize()
   ```

3. **Visualize from Dictionary**

   If you have a result dictionary from the benchmark:

   ```python
   from BenchmarkVisualizer import BenchmarkVisualizer

   result = {
       'RecursiveFibonacci': {'times': [...], 'average': ..., 'min': ..., 'max': ...},
       'GMPDoublingFibonacci': {'times': [...], 'average': ..., 'min': ..., 'max': ...},
       # Add more strategies as needed
   }

   visualizer = BenchmarkVisualizer(result, 'benchmark_plot_from_dict.png')
   visualizer.visualize()
   ```

## Supported Strategies

- **RecursiveFibonacci**: A simple recursive implementation of Fibonacci calculation.
- **IterativeFibonacci**: An iterative approach to calculating Fibonacci numbers.
- **MatrixFibonacci**: A matrix-based strategy for efficient Fibonacci computation.
- **ImprovedMatrixFibonacci**: An optimized version of the matrix strategy.
- **DoublingFibonacci**: A strategy using doubling to calculate Fibonacci numbers.
- **GMPIterativeFibonacci**: An iterative strategy using GMP (GNU Multiple Precision Arithmetic Library).
- **GMPMatrixFibonacci**: A matrix-based strategy using GMP for efficient calculations.
- **GMPImprovedMatrixFibonacci**: An optimized version of the GMP matrix strategy.
- **GMPDoublingFibonacci**: An optimized strategy using GMP (GNU Multiple Precision Arithmetic Library) for efficient calculations.
- **GMPDoublingFibonacciOptimized**: Further optimized version of the GMP doubling strategy.

*Feel free to add more strategies by implementing the `execute` method in new classes and adding them to the benchmark.*

## Configuration

You can configure the benchmarking parameters by modifying the `run_fibonacci_benchmark` function in `FibonacciBenchmark.py`:

- **max_n**: The highest Fibonacci number to compute.
- **spread**: The interval between successive Fibonacci numbers to benchmark.
- **timeout**: The maximum allowed time for each computation before it is aborted.
- **strategies**: List of strategy instances to include in the benchmark.
- **csv_filename**: Filename for exporting results to CSV.
- **json_filename**: Filename for exporting results to JSON.
