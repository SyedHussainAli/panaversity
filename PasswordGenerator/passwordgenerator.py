import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

number = int(input('Enter the number of passwords you want to generate: '))
length = int(input('Enter the length of the password: '))
passwords = []
print("\n\n\n__________________________________________________")
print('Generating passwords...')
print('Here are the passwords: ')

for i in range(number):
    password = ''.join(random.choices(all_chars, k=length))
    passwords.append(password)
    print(passwords[i])