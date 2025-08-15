import csv
import json

csv_file = 'total2.csv'  # Replace with your CSV file path
json_file = 'total2.json'  # Output JSON file

data = {}

with open(csv_file, 'r') as csvf:
    csv_reader = csv.DictReader(csvf)
    for row in csv_reader:
        strategy = row['strategy']
        n = int(row['n'])
        time = float(row['time'])

        if strategy not in data:
            data[strategy] = []
        data[strategy].append({'n': n, 'time': time})

# Sort the data by 'n' for each strategy
for strategy in data:
    data[strategy] = sorted(data[strategy], key=lambda x: x['n'])

with open(json_file, 'w') as jsonf:
    json.dump(data, jsonf, indent=4)
