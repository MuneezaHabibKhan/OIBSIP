import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "You must select at least one character type!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Random Password Generator 🔐")

length = int(input("Enter password length: "))

print("Include:")
use_letters = input("Letters? (y/n): ").lower() == "y"
use_numbers = input("Numbers? (y/n): ").lower() == "y"
use_symbols = input("Symbols? (y/n): ").lower() == "y"

password = generate_password(length, use_letters, use_numbers, use_symbols)

print("\nGenerated Password:")
print(password)
