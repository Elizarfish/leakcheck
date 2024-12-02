# LeakCheck API Client

A Python client for using the LeakCheck API with support for both API v1 and v2.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Elizarfish/leakcheck.git
```

2. Navigate to the project directory:
```bash
cd leakcheck
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## API Versions

The repository contains two versions of the client:
- `leakcheck.py` - Client for LeakCheck API v1
- `leakcheck_v2.py` - Client for LeakCheck API v2 with enhanced features

## Configuration

Before using either version, you need to set your API key:

### For API v1 (leakcheck.py)
Open the `leakcheck.py` file and replace:
```python
API_KEY = ""
```

### For API v2 (leakcheck_v2.py)
Open the `leakcheck_v2.py` file and replace:
```python
API_KEY = "API_KEY"
```

with your LeakCheck API key.

## Usage

### API v1 Client (leakcheck.py)

1. Create a CSV file with search queries, each query on a separate line:
```
example@example.com
example2@example.com
example3@example.com
```

2. Run the script:
```bash
python leakcheck.py -f input.csv -t email -o output.csv
```

Available arguments:
- `-f`, `--file`: Path to the input file with queries
- `-t`, `--type`: Search type (email, mass, hash, pass_email, phash, domain_email, login, phone, mc, pass_login, pass_phone, auto)
- `-o`, `--output`: Path to the output file

### API v2 Client (leakcheck_v2.py)

The v2 client supports both single queries and batch processing from a file.

#### Single Query:
```bash
python leakcheck_v2.py -i example@example.com -t email -o results.txt
```

#### Multiple Queries from File:
```bash
python leakcheck_v2.py -iL queries.txt -t auto -o results.txt
```

Available arguments:
- `-i`, `--input`: Single query (email, domain, phone, etc.)
- `-iL`, `--input-list`: Path to file with list of queries
- `-t`, `--query-type`: Query type (auto, email, domain, phone, username, hash, keyword, etc.)
- `-o`, `--output`: Path to output file for results

The v2 client includes enhanced features:
- Improved error handling
- Rate limiting support
- More detailed result formatting
- Quota monitoring
- Additional data fields support (username, phone, first/last name)

## Requirements

- Python 3.x
- requests

## Error Handling

Both clients include error handling for common issues:
- HTTP errors
- SSL errors
- API rate limits
- Invalid queries

## Note

Make sure to comply with LeakCheck's API usage limits and terms of service when using either client.

For more information about the LeakCheck API, visit their official documentation.
