import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


no_letters= int(input("How many letters would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like?\n"))
no_symbols = int(input("How many Symbols would you like?"))

length_of_pass = no_letters + no_numbers + no_symbols

password = []

for i in range(no_letters):
    password.append(random.choice(letters))
for i in range(no_numbers):
    password.append(random.choice(numbers))
for i in range(no_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

final_pass= ''.join(password)
print(f"Here is your password: {final_pass}")
