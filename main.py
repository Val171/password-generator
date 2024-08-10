letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '-']
print("PW Genner")
n_let = int(input("How many letters?:\n"))
n_num = int(input("How many numbers?:\n"))
n_char = int(input("How many special characters?:\n"))
import random

pw = []
for i in range(0, n_let):
    pw.append(random.choice(letter))
for i in range(0, n_num):
    pw.append(random.choice(num))
for i in range(0, n_char):
    pw.append(random.choice(char))

random.shuffle(pw)
print("".join(pw))
