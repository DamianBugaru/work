"""Calculate column-wise averages from a CSV file."""

import argparse
import csv

def calculate_averages(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        totals = {}
        counts = {}

        for row in reader:
            for key, value in row.items():
                try:
                    num = float(value)
                    totals[key] = totals.get(key, 0.0) + num
                    counts[key] = counts.get(key, 0) + 1
                except ValueError:
                    continue  # skip non-numeric data

        averages = {key: totals[key] / counts[key] for key in totals}
        return averages

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate averages for each numeric column in a CSV file"
    )
    parser.add_argument("csvfile", help="Path to the CSV file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    averages = calculate_averages(args.csvfile)
    for column, avg in averages.items():
        print(f"{column}: {avg:.2f}")
