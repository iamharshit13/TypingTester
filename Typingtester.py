import random
# import keyboard
from pynput import keyboard

file1= open("words.txt","r")
l=[]
for line in file1:
    ls = line.strip()
    l.append(str(ls))

len(l)

fullt=[]

random.shuffle(l)
for line in range(1,1001,10):
    fullt.append(l[line:line+10])

len(fullt)

for linen in fullt:
    print(*linen,sep=', ')
    for wordn in linen:
        print()
        for letter in wordn:
            print(letter)
