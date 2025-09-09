import json
import csv


INPUT_FILE = "../data/grammy_awards.json"
OUTPUT_FILE = "../data/grammy_awards.csv"



with open(INPUT_FILE, "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Extract header keys from first JSON object
headers = data[0].keys()

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print(f"JSON converted → {OUTPUT_FILE} ({len(data)} records)")
