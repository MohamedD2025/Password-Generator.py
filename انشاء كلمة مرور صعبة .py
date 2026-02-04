import random
import string
print("***welcome to the password generator***")
length=int(input("enter the length of the password \n"))

num_letters=int(input("what is the number of the letters that you want the password contain? \n"))
num_digits=int(input("what is the number of the digits that you want the password contain? \n"))
num_symbols=int(input("what is the number of the symbols that you want the password contain? \n"))

if length==(
    num_letters+num_digits+num_symbols
):
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation

    password_chars=(
        random.choices(letters, k=num_letters)+
        random.choices(digits, k=num_digits)+
        random.choices(symbols, k=num_symbols)
    )
    
    random.shuffle(password_chars)

    password="".join(password_chars)
    print("generated password:" + password)
else:
    print("invalid choice")







    




