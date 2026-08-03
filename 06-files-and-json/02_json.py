"""
JSON (JavaScript Object Notation)

The format almost every REST API uses.
Python ↔ JSON via the built-in `json` module.

Memory trick — the extra "s" means string:
  dump / load   → file
  dumps / loads → string
"""

import json
from pathlib import Path

DIR = Path(__file__).parent
SAMPLE = DIR / "sample.json"
CONFIG = DIR / "config.json"


# ------------------------------------------------------------
# JSON vs Python (look similar, not identical)
# ------------------------------------------------------------
# Python True/False/None  →  JSON true/false/null
# JSON strings always use double quotes


# ------------------------------------------------------------
# dict → JSON string — dumps()
# ------------------------------------------------------------
user = {
    "name": "Yog",
    "age": 25,
    "is_admin": True,
}

json_string = json.dumps(user)
print(json_string)
print(type(user))  # <class 'dict'>
print(type(json_string))  # <class 'str'>
print()


# ------------------------------------------------------------
# Pretty printing — indent=
# ------------------------------------------------------------
pretty = json.dumps(user, indent=4)
print(pretty)
print()


# ------------------------------------------------------------
# JSON string → dict — loads()
# ------------------------------------------------------------
api_response = """
{
    "id": 1,
    "name": "Yog",
    "email": "yog@example.com"
}
"""

parsed = json.loads(api_response)
print(parsed)
print(parsed["email"])
print(type(parsed))  # <class 'dict'>
print()


# ------------------------------------------------------------
# Real backend-ish — save / load config file
# ------------------------------------------------------------
config = {
    "host": "localhost",
    "port": 5432,
}

with open(CONFIG, "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)

with open(CONFIG, encoding="utf-8") as file:
    loaded_config = json.load(file)

print(loaded_config["host"])
print()


# ------------------------------------------------------------
# Quick reference
# ------------------------------------------------------------
# dump(obj, file)  — write Python → JSON file
# load(file)       — read JSON file → Python
# dumps(obj)       — Python → JSON string
# loads(string)    — JSON string → Python


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# 1. Create user dict with name, age, skills
# 2. Write to sample.json with dump(..., indent=4)
# 3. Read it back with load() and print
# 4. dumps() → print type (str)
# 5. loads() → print type (dict)


user = {
    "name": "Yog",
    "age": 25,
    "skills": [
        "Python",
        "FastAPI",
        "Docker",
    ],
}

with open(SAMPLE, "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)

with open(SAMPLE, encoding="utf-8") as file:
    user = json.load(file)

print(user)
print()

json_string = json.dumps(user, indent=4)
print(json_string)
print(type(json_string))  # <class 'str'>
print()

user_dict = json.loads(json_string)
print(user_dict)
print(type(user_dict))  # <class 'dict'>
