import requests
import argparse
import csv
import time

API_KEY = ""

def make_request(check_type, query):
    url = f"https://leakcheck.io/api?key={API_KEY}&check={query}&type={check_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

def process_file(file_path, check_type, output_file):
    with open(file_path, newline='') as csvfile, open(output_file, 'w') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        for row in reader:
            query = row[0]
            result = make_request(check_type, query)
            print(f"Result for {query}:")
            if result.get('result'):
                for entry in result['result']:
                    line = entry.get('line', '')
                    sources = ', '.join(entry.get('sources', []))
                    print(f"\t{line} | Sources: {sources}")
                    writer.writerow([line, sources])
            else:
                print(result)
            time.sleep(0.5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LeakCheck API Client")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the file containing search queries")
    parser.add_argument("-t", "--type", type=str, required=True, help="Search type: email, mass, hash, pass_email, phash, domain_email, login, phone, mc, pass_login, pass_phone, auto")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to the output file for results")
    args = parser.parse_args()

    process_file(args.file, args.type, args.output)
