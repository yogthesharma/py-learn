# challange 1
numbers = [number for number in range(1, 6)]

print(numbers)
print()

# challange 2
numbers_2 = [1, 2, 3, 4, 5]
numbers_2_sqrd = [number**2 for number in numbers_2]

print(numbers_2_sqrd)
print()

# challange 3
numbers_odd = [number for number in range(20) if number % 2 != 0]
print(numbers_odd)
print()

# challange 4
languages = ["Python", "Rust", "Go"]
languages_uppercase = [language.upper() for language in languages]
print(languages_uppercase)
print()

# bonus
even_odd = ["even" if number % 2 == 0 else "odd" for number in range(5)]
print(even_odd)
