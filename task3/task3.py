import json
import sys

def find_and_fill(test, values):
    if 'id' in test:
        for value in values:
            if value['id'] == test['id']:
                test['value'] = value['value']
                break
    if 'values' in test:
        for item in test['values']:
            find_and_fill(item, values)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py values.json tests.json report.json")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        values = json.load(f)['values']

    with open(sys.argv[2], 'r') as f:
        tests = json.load(f)['tests']

    find_and_fill(tests, values)

    with open(sys.argv[3], 'w') as f:
        json.dump(tests, f, indent=2)
