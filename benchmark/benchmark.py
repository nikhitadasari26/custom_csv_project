import csv
import time
from custom_csv.reader import CustomCsvReader
from custom_csv.writer import CustomCsvWriter


def benchmark_reader():
    start = time.time()
    with open("benchmark_data.csv", "r") as f:
        reader = CustomCsvReader(f)
        for _ in reader:
            pass
    return time.time() - start


def benchmark_csv_reader():
    start = time.time()
    with open("benchmark_data.csv", "r") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass
    return time.time() - start


if __name__ == "__main__":
    custom_time = benchmark_reader()
    standard_time = benchmark_csv_reader()

    print(f"Custom Reader Time: {custom_time:.4f} seconds")
    print(f"csv.reader Time: {standard_time:.4f} seconds")
