"""
CSV (Comma-Separated Values)

The format behind "Export Users" / "Download Report" buttons.
Use the built-in `csv` module — don't hand-write commas.

Always open CSV files with newline="" (avoids blank rows on Windows)
and encoding="utf-8".

Prefer DictReader / DictWriter when you have named columns.
"""

import csv
from pathlib import Path

DIR = Path(__file__).parent
SAMPLE = DIR / "sample.csv"
EXPORT = DIR / "users_export.csv"


# ------------------------------------------------------------
# Writing rows — csv.writer
# ------------------------------------------------------------
with open(SAMPLE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Yog", 25, "Gurgaon"])
    writer.writerow(["Alice", 30, "London"])

print("Wrote sample.csv with csv.writer")
print()


# ------------------------------------------------------------
# Reading rows — csv.reader
# ------------------------------------------------------------
# Everything comes back as str (CSV has no int/bool/float types)
print("--- csv.reader ---")
with open(SAMPLE, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()


# ------------------------------------------------------------
# Reading as dicts — csv.DictReader
# ------------------------------------------------------------
print("--- csv.DictReader ---")
with open(SAMPLE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["Name"])  # nicer than row[0]
print()


# ------------------------------------------------------------
# Writing dicts — csv.DictWriter
# ------------------------------------------------------------
users = [
    {"Name": "Yog", "Age": 25, "City": "Gurgaon"},
    {"Name": "Alice", "Age": 30, "City": "London"},
]

with open(SAMPLE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(users)

print("Rewrote sample.csv with csv.DictWriter")
print()


# ------------------------------------------------------------
# Real backend-ish — export users for download
# ------------------------------------------------------------
export_users = [
    {"Name": "Yog", "Email": "yog@example.com"},
    {"Name": "Alice", "Email": "alice@example.com"},
]

with open(EXPORT, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Email"])
    writer.writeheader()
    writer.writerows(export_users)

print("Wrote users_export.csv")
print()


# ------------------------------------------------------------
# Quick reference
# ------------------------------------------------------------
# csv.writer / csv.reader         → list rows
# csv.DictWriter / csv.DictReader → dict rows (prefer these)


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# 1. Create users list (Yog, Alice, Bob)
# 2. Write with DictWriter + writeheader()
# 3. Read with DictReader and print each user
# 4. Read again with csv.reader and print each row


users = [
    {"Name": "Yog", "Age": 25, "City": "Gurgaon"},
    {"Name": "Alice", "Age": 30, "City": "London"},
    {"Name": "Bob", "Age": 28, "City": "New York"},
]

with open(SAMPLE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(users)

print("--- Challenge: DictReader ---")
with open(SAMPLE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for user in reader:
        print(user)
print()

print("--- Challenge: csv.reader ---")
with open(SAMPLE, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
