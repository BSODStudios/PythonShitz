import random
import time
import sys
import string
let = string.ascii_lowercase
num = string.digits
a=0
b=0
c=0
d=0
e=0
time.sleep(random.randint(0,1))
print("Password 1:  ", end="")
while a<7:
    letran=random.choice(let)
    numran=random.choice(num)
    ran=[letran,numran]
    random.shuffle(ran)
    ranF=''.join(ran)
    print(ranF, end="")
    
    a+=1
print("\n")
time.sleep(random.randint(0,1))
print("Password 2:  ", end="")
while b<7:
    letran=random.choice(let)
    numran=random.choice(num)
    ran=[letran,numran]
    random.shuffle(ran)
    ranF=''.join(ran)
    print(ranF, end="")
    b+=1
print("\n")
time.sleep(random.randint(0,1))
print("Password 3:  ", end="")
while c<7:
    letran=random.choice(let)
    numran=random.choice(num)
    ran=[letran,numran]
    random.shuffle(ran)
    ranF=''.join(ran)
    print(ranF, end="")
    c+=1
print("\n")
time.sleep(random.randint(0,1))
print("Password 4:  ", end="")
while d<7:
    letran=random.choice(let)
    numran=random.choice(num)
    ran=[letran,numran]
    random.shuffle(ran)
    ranF=''.join(ran)
    print(ranF, end="")
    d+=1
print("\n")
time.sleep(random.randint(0,1))
print("Password 5:  ", end="")
while e<7:
    letran=random.choice(let)
    numran=random.choice(num)
    ran=[letran,numran]
    random.shuffle(ran)
    ranF=''.join(ran)
    print(ranF, end="")
    e+=1
input("")
