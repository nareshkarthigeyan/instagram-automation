import json
import os

path = "/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/content.txt"
JsonPath = "/home/nareshkarthigeyan/Naresh/cs/code/intagramautomater-python/content.json"

if os.path.exists(path):
    with open(path, "r") as f:
        text = f.read()
        data = text.split("\n")
        data = [line.replace('"', '') for line in data if line.strip()]
        print(data)

    if os.path.exists(JsonPath):
        with open(JsonPath, "r") as f:
            try:
                oldData = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: {JsonPath} is not a valid JSON file.")
                oldData = {"quotes": []}
    else:
        oldData = {"quotes": []}
    next_id = max(quote['id'] for quote in oldData['quotes']) + 1 if oldData['quotes'] else 1
    for quote_text in data:
        new_quote = {
            "id": next_id,
            "quote": quote_text
        }
        oldData['quotes'].append(new_quote)
        next_id += 1
    for quote in oldData['quotes']:
        print(f"ID: {quote['id']}, Quote: {quote['quote']}")
    with open(JsonPath, "w") as f:
        json.dump(oldData, f, indent=4)
else:
    print(f"File not found: {path}")
