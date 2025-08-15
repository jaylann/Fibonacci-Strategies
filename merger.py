import csv
import argparse
import sys
from collections import defaultdict

def merge_csv_files_builtin(file_list, output_file):
    """
    Merges multiple CSV files by averaging the 'time' for duplicate 'strategy' and 'n' entries using the built-in csv module.

    Parameters:
    - file_list: List of input CSV file paths.
    - output_file: Path to the output CSV file.
    """
    data = defaultdict(list)

    for file in file_list:
        try:
            with open(file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                # Check for required columns
                if not {'strategy', 'n', 'time'}.issubset(reader.fieldnames):
                    print(f"Error: File {file} does not contain required columns.", file=sys.stderr)
                    continue
                for row in reader:
                    key = (row['strategy'], row['n'])
                    try:
                        time_val = float(row['time'])
                        data[key].append(time_val)
                    except ValueError:
                        print(f"Warning: Invalid time value in file {file}, row {row}", file=sys.stderr)
        except Exception as e:
            print(f"Error reading {file}: {e}", file=sys.stderr)

    if not data:
        print("No valid data to process.", file=sys.stderr)
        return

    # Compute average times
    merged_data = []
    for (strategy, n), times in data.items():
        avg_time = sum(times) / len(times)
        merged_data.append({'strategy': strategy, 'n': n, 'time': avg_time})

    # Sort merged data
    merged_data.sort(key=lambda x: (x['strategy'], int(x['n'])))

    # Write to output CSV
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['strategy', 'n', 'time'])
            writer.writeheader()
            for row in merged_data:
                writer.writerow(row)
        print(f"Merged CSV saved to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Merge CSV files by averaging times for identical strategy and n using built-in csv module.')
    parser.add_argument('input_files', nargs='+', help='List of input CSV files to merge.')
    parser.add_argument('-o', '--output', default='merged_output.csv', help='Output CSV file name (default: merged_output.csv)')

    args = parser.parse_args()

    merge_csv_files_builtin(args.input_files, args.output)

if __name__ == '__main__':
    main()
