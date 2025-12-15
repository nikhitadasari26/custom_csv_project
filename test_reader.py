from custom_csv.reader import CustomCsvReader

with open("tests/test.csv", "r") as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)
