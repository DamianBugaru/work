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

if __name__ == "__main__":
    filename = "data.csv"  # replace with your CSV filename
    averages = calculate_averages(filename)
    for column, avg in averages.items():
        print(f"{column}: {avg:.2f}")
