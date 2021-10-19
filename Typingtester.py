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

"""
This section is still under development
will keep updating
"""
# taking values directly from keyboard
def on_press(key):
    try:
        if key == 'q':
            pass
        else:
            print("wrong")
    except Error:
        print(Error)

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
    
    
    
# For GUI Tkinter is used
# Will develop this in the end
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
