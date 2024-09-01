import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from typing import Union, Dict, Any
import logging

class BenchmarkVisualizer:
    """
    A class for visualizing benchmark results from Fibonacci calculations.
    """

    def __init__(self, data_source: Union[str, Dict[str, Any]], output_file: str = 'benchmark_plot.png'):
        """
        Initialize the BenchmarkVisualizer.

        :param data_source: Either a path to a CSV file or a result object from FibonacciBenchmark.
        :param output_file: Name of the output plot file.
        """
        self.data_source = data_source
        self.output_file = output_file
        self.data = None
        self.grouped = None
        self.logger = self._setup_logger()

    @staticmethod
    def _setup_logger():
        """Set up and return a logger for the class."""
        logger = logging.getLogger('BenchmarkVisualizer')
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    def load_data(self):
        """Load and process the benchmark data."""
        if isinstance(self.data_source, str):
            self._load_from_csv()
        elif isinstance(self.data_source, dict):
            self._load_from_dict()
        else:
            raise ValueError("Invalid data source. Must be a file path or a result dictionary.")

        self.grouped = self.data.groupby('strategy')

    def _load_from_csv(self):
        """Load data from a CSV file."""
        try:
            self.data = pd.read_csv(self.data_source)
        except Exception as e:
            self.logger.error(f"Error loading CSV file: {e}")
            raise

    def _load_from_dict(self):
        """Load data from a result dictionary."""
        try:
            data_list = []
            for strategy, result in self.data_source.items():
                for n, time in enumerate(result['times']):
                    data_list.append({'strategy': strategy, 'n': n, 'time': time})
            self.data = pd.DataFrame(data_list)
        except Exception as e:
            self.logger.error(f"Error processing result dictionary: {e}")
            raise

    def create_plot(self):
        """Create and save the benchmark plot."""
        if self.data is None:
            self.load_data()

        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(20, 12), dpi=300)

        colors = plt.cm.viridis(np.linspace(0, 1, len(self.grouped)))

        for (strategy, group), color in zip(self.grouped, colors):
            self._plot_strategy(ax, strategy, group, color)

        self._customize_plot(ax)
        self._save_plot(fig)

    def _plot_strategy(self, ax, strategy: str, group: pd.DataFrame, color: np.ndarray):
        """Plot data for a single strategy."""
        group = group.sort_values('n')
        x, y = group['n'].values, group['time'].values

        if len(x) > 2:
            self._plot_interpolated(ax, x, y, strategy, color)
        else:
            ax.plot(x, y, label=strategy, linewidth=1, color=color)

        ax.scatter(x, y, s=1, color=color, alpha=0.6, zorder=2)

    def _plot_interpolated(self, ax, x: np.ndarray, y: np.ndarray, strategy: str, color: np.ndarray):
        """Plot interpolated data for smoother curves."""
        x_smooth = np.linspace(x.min(), x.max(), 300)
        try:
            interp_func = interp1d(x, y, kind='linear')
            y_smooth = interp_func(x_smooth)
            ax.plot(x_smooth, y_smooth, label=strategy, linewidth=1, color=color)
        except ValueError:
            self.logger.warning(f"Interpolation failed for {strategy}. Plotting raw data.")
            ax.plot(x, y, label=strategy, linewidth=1, color=color)

    def _customize_plot(self, ax):
        """Apply customizations to the plot."""
        ax.set_xlabel('n', fontsize=16, fontweight='bold')
        ax.set_ylabel('Time', fontsize=16, fontweight='bold')
        ax.set_title('Time vs n for Different Strategies', fontsize=20, fontweight='bold')

        ax.legend(fontsize=14, loc='center left', bbox_to_anchor=(1, 0.5),
                  frameon=True, fancybox=True, shadow=True)

        ax.grid(True, linestyle='--', alpha=0.7)
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.minorticks_on()
        ax.grid(which='minor', linestyle=':', alpha=0.4)

        # Uncomment the following line to use logarithmic scale if needed
        # ax.set_yscale('log')

    def _save_plot(self, fig):
        """Save the plot to a file."""
        try:
            fig.tight_layout()
            fig.savefig(self.output_file, dpi=300, bbox_inches='tight')
            self.logger.info(f"Plot saved as {self.output_file}")
        except Exception as e:
            self.logger.error(f"Error saving plot: {e}")
        finally:
            plt.close(fig)

    def visualize(self):
        """Main method to create and save the visualization."""
        self.load_data()
        self.create_plot()

# Example usage:
if __name__ == "__main__":
    # Using a CSV file
    visualizer = BenchmarkVisualizer('results.csv', 'benchmark_plot_from_csv.png')
    visualizer.visualize()

    # Using a result dictionary (assuming you have run the benchmark)
    # from your_benchmark_module import run_fibonacci_benchmark
    # result = run_fibonacci_benchmark(...)  # Run your benchmark
    # visualizer = BenchmarkVisualizer(result, 'benchmark_plot_from_dict.png')
    # visualizer.visualize()