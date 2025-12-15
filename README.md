<<<<<<< HEAD
# Custom CSV Reader and Writer

## Overview

This project creates a CSV reader and writer using Python without using the
built-in csv module. The purpose of this project is to learn how CSV files are
read and written internally.

The implementation correctly handles special cases such as values inside
quotes, double quotes inside text, commas inside values, and values that
contain new lines.

## Project Structure 
CUSTOM_CSV_PROJECT/
│
├── benchmark/
│   |── benchmark.py
│   ├── generate_data.py
│   └── __pycache__/
│
├── custom_csv/
│   ├── __init__.py
│   ├── reader.py
│   ├── writer.py
│   └── __pycache__/
│
├── tests/
│   └── test.csv
│
├── benchmark_data.csv
├── README.md
├── requirements.txt
├── test_reader.py


## Setup Instructions
1. Make sure Python 3 is installed on your system.
2. Download or clone this project.
3. Open a terminal and go to the project folder.

Run the following commands:

```bash
python benchmark/generate_data.py
python -m benchmark.benchmark

```

=======
# custom_csv_project
>>>>>>> 8e5ffb72132ed8545892798695ccf83fb1c88b4b
