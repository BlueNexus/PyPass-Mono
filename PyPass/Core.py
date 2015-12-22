import random
import string

valList = list(string.ascii_letters + string.digits)

def generate(valList, length):
    password = []
    for char in range(1, length + 1):
        password.append(str(valList[random.randint(1, 61)]))
    print "".join(password)

while True:
    length = int(raw_input("How long should the password be?"))
    generate(valList, length)
