def generate_csv(path, rows=10000, cols=5):
    with open(path, "w") as f:
        for i in range(rows):
            row = [f"value_{i}_{j}" for j in range(cols)]
            f.write(",".join(row) + "\n")


if __name__ == "__main__":
    generate_csv("benchmark_data.csv")
