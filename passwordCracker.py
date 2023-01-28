import string
import time
import sys

class Bcolors:
    RED = '\u001b[31m'
    GREEN = ' \u001b[32m'
    YELLOW = '\u001b[33m'

maxattempts = 10000000000
start = time.time()
chars = (string.digits + string.ascii_letters + string.punctuation)[:95]
base = len(chars)
n = 0
solved = False
password = input(Bcolors.GREEN + "Enter a Password <: ")

if password == '':
    print(Bcolors.RED + "Password is Empty, please enter a password!")
    solved = True
    sys.exit(1)

def crackPassword(n, base):
    digits = []
    while n:
        digits.append(n % base)
        n = n // base #dividing the number and storing it in the n in a round integer
    return digits


while n < maxattempts:
    lst = crackPassword(n, base)
    word = ''
    for x in lst:
        word += str(chars[x])
        # print(word)
    if password == word:
        solved = True
        print(Bcolors.YELLOW + "--Stats--")
        print(Bcolors.GREEN + "Password is " + word)
        print(Bcolors.GREEN + f"Attempts: {str(n)}")
        print(Bcolors.GREEN + f"Time took: {str(round(time.time() - start , 2))} seconds")
        sys.exit(0)
      
    else:
        n += 1

if password not in str(maxattempts):
    print(Bcolors.RED +f"Unresolved Password after: {str(n)} attempts")