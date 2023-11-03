# LeakCheck API Client

A simple Python client for using the LeakCheck API.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Elizarfish/leakcheck-api-client.git
```

2. Navigate to the project directory:
```bash
cd leakcheck-api-client
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Open the `leakcheck.py` file and replace the following line:

```python
API_KEY = "YOUR_KEY"
```

with your LeakCheck API key.

## Usage
1. Create a CSV file with search queries, each query on a separate line. For example:
```graphql
example@example.com
example2@example.com
example3@example.com
```

2. Run the script with the appropriate arguments. Replace `input.csv`, `email`, and `output.csv` with your input file, search type, and output file, respectively:
```bash
python leakcheck.py -f input.csv -t email -o output.csv
```

This will process the queries from `input.csv`, search for leaks of type `email`, and save the results to `output.csv`.

Refer to the help message for more information on available search types:
```bash
python leakcheck.py -h
```
