"""
Variables

Names that point at values in memory. Python figures out the type from
what you assign — no `int x` declarations.

Use f-strings (`f"{name}"`) for readable output; `.capitalize()` / `.title()`
format strings without changing the stored value.

Gotcha: reassigning a name binds it to a new value; it does not mutate
the old object unless the object itself is mutable (lists, dicts, etc.).
"""

name = "Yog Sharma"
age = 26
expirence = 6
city = "gurugram"
country = "india"
favourite_language = "javascript"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Expirence: {expirence}")
print(f"City: {city.capitalize()}")
print(f"Country: {country.capitalize()}")
print(f"Favourite Language: {favourite_language.capitalize()}")