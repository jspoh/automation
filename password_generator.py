# simple password generator

import random

password = ""
l_pass = []
s_pass = []
n_pass = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol = "`~!@#$%^&*()_+-=[]\{}|;':\",./<>?"

letters = int(input("Number of letters: "))
symbols = int(input("Number of symbols: "))
numbers = int(input("Number of numbers: "))

for i in range(letters):
    l = random.randint(0, len(alphabet)-1)
    ul = random.randint(0, 1)
    if ul == 0:
        l_pass.append(alphabet[l])
    else:
        l_pass.append(alphabet[l].upper())

for i in range(symbols):
    s = random.randint(0, len(symbol)-1)
    s_pass.append(symbol[s])

for i in range(numbers):
    n = random.randint(0, 9)
    n_pass.append(str(n))

counter = 0
while counter < letters+symbols+numbers:
    choice = random.randint(1, 3)
    if choice == 1:
        if l_pass:
            lc = random.randint(0, len(l_pass)-1)
            password += l_pass[lc]
            l_pass.remove(l_pass[lc])
            counter += 1
    elif choice == 2:
        if s_pass:
            ls = random.randint(0, len(s_pass) - 1)
            password += s_pass[ls]
            s_pass.remove(s_pass[ls])
            counter += 1
    else:
        if n_pass:
            ln = random.randint(0, len(n_pass)-1)
            password += n_pass[ln]
            n_pass.remove(n_pass[ln])
            counter += 1

print(password)
