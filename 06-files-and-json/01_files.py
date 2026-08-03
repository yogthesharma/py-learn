"""
Files

Variables live in memory — when the program ends, they're gone.
Files let you persist data: logs, configs, reports, templates.

Always prefer:
  with open(...) as file:
Python closes the file automatically when the block ends.

Always pass encoding="utf-8" — OS defaults differ; UTF-8 is the standard.
"""

from pathlib import Path

# Resolve paths next to this script (works from any working directory)
DIR = Path(__file__).parent
SAMPLE = DIR / "sample.txt"
NOTES = DIR / "notes.txt"


# ------------------------------------------------------------
# Modes (you'll mostly use the first three)
# ------------------------------------------------------------
# "r"  — read (file must exist)
# "w"  — write (creates file, OVERWRITES existing content)
# "a"  — append (add to the end, keeps existing content)
# "x"  — create new file only (fails if it already exists)
# "rb" / "wb" — binary read / write


# ------------------------------------------------------------
# Writing with "w"
# ------------------------------------------------------------
with open(NOTES, "w", encoding="utf-8") as file:
    file.write("User logged in\n")

print("Wrote notes.txt")
print()


# ------------------------------------------------------------
# Appending with "a"
# ------------------------------------------------------------
with open(NOTES, "a", encoding="utf-8") as file:
    file.write("User logged out\n")

print("Appended to notes.txt")
print()


# ------------------------------------------------------------
# Reading the whole file — read()
# ------------------------------------------------------------
with open(NOTES, "r", encoding="utf-8") as file:
    content = file.read()

print("--- notes.txt (read) ---")
print(content)


# ------------------------------------------------------------
# Reading line by line
# ------------------------------------------------------------
# strip() removes the trailing \n (and other whitespace)
print("--- notes.txt (line by line) ---")
with open(NOTES, encoding="utf-8") as file:  # "r" is the default
    for line in file:
        print(line.strip())
print()


# ------------------------------------------------------------
# Reading all lines into a list — readlines()
# ------------------------------------------------------------
with open(NOTES, encoding="utf-8") as file:
    lines = file.readlines()

print(lines)  # ['User logged in\n', 'User logged out\n']
print()


# ------------------------------------------------------------
# Real backend-ish uses
# ------------------------------------------------------------
# logs:     open("logs.txt", "a", encoding="utf-8")
# prompts:  open("prompt.txt", encoding="utf-8").read()
# SQL:      open("schema.sql", encoding="utf-8").read()
# emails:   open("email.md", encoding="utf-8").read()


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# 1. Write three lines to sample.txt
# 2. Read the whole file with read()
# 3. Read line by line with a for loop
# 4. Append: See you tomorrow!
# 5. Read once more to verify


with open(SAMPLE, "w", encoding="utf-8") as file:
    file.write("Hello Yog\n")
    file.write("Welcome to Python\n")
    file.write("Files are awesome\n")

print("--- sample.txt after write ---")
with open(SAMPLE, encoding="utf-8") as file:
    print(file.read())

print("--- sample.txt line by line ---")
with open(SAMPLE, encoding="utf-8") as file:
    for line in file:
        print(line.strip())
print()

with open(SAMPLE, "a", encoding="utf-8") as file:
    file.write("See you tomorrow!\n")

print("--- sample.txt after append ---")
with open(SAMPLE, encoding="utf-8") as file:
    print(file.read())
