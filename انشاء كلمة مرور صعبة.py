import random
import string
print("welcome to the password generator")
length=int(input("enter the length of the password \n"))
num_letters=int(input("enter the number of letters that you want to exist in the password \n"))
num_numbers=int(input("enter the number of numbers in the password \n"))
num_symbols=int(input("enter the number of symbols in the password \n"))
if length != (num_letters+num_numbers+num_symbols):
    print("please commet to the rules")
else:
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    password_chars=(
        random.choices(letters,k=num_letters) +
        random.choices(numbers, k=num_numbers) +
        random.choices(symbols,  k=num_symbols)
    )
    random.shuffle(password_chars)
    print(password_chars)
    password= "".join(password_chars)
    print("this is the generated password:" + password)

