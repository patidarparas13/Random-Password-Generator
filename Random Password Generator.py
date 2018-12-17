import string
import random
char = string.printable
print(char)
nop = int(input("No. of Password:"))
length = int(input("Password Length?"))

for p in range(nop):
  password = ''
  for c in range(length):
    password += random.choice(char)
  print(password)
