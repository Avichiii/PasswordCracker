import string
import time
import sys

maxattempts = 10000000000
start = time.time()
chars = (string.digits + string.ascii_letters + string.punctuation)[:95]
base = len(chars)
n = 0
solved = False
password = input("Enter a Password <: ")


def crackPassword(n, base):
    digits = []
    while n:
        digits.append(n % base)
        n = n // base #dividing the number and storing it in the n in a round integer
    return digits


if password == '':
    print("Password is Empty, please enter a password!")
    solved = True
    sys.exit(1)


while n < maxattempts:
    lst = crackPassword(n, base)
    word = ''
    for x in lst:
        word += str(chars[x])
        # print(word)
    if password == word:
        solved = True
        print("--Stats--")
        print("Password is " + word)
        print(f"Attempts: {str(n)}")
        print(f"Time took: {str(round(time.time() - start , 2))} seconds")
        sys.exit(0)
    else:
        n += 1

if password not in str(maxattempts):
    print(f"Unresolved Password after: {str(n)} attempts")