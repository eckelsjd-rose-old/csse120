import time
from tkinter import *


def main():

    root = Tk()

    button1 = Button(root, text='Press w')
    button1['command'] = lambda: forward_callback('hello')
    button1.grid(row=0, column=0)
    root.bind('<w>', forward_callback)

    button2 = Button(root, text='Press a')
    button2['command'] = lambda: left_callback()
    button2.grid(row=0, column=1)
    root.bind('<a>', left_callback)

    button3 = Button(root, text='Press d')
    button3['command'] = lambda: right_callback()
    button3.grid(row=0, column=2)
    root.bind('<d>', right_callback)

    button4 = Button(root, text='Press q')
    button4['command'] = lambda: quit_program()
    button4.grid(row=1, column=0)
    root.bind('<q>', quit_program)

    button5 = Button(root, text='Press spacebar')
    button5['command'] = lambda: powerup_callback()
    button5.grid(row=1, column=2)
    root.bind('<space>', powerup_callback)

    root.mainloop()


def forward_callback(value, event=None):
    print(value)
    time.sleep(.1)


def left_callback(event=None):
    print('left')
    time.sleep(.1)


def right_callback(event=None):
    print('right')
    time.sleep(.1)


def powerup_callback(event=None):
    print('powerup')
    time.sleep(.1)


def quit_program(event=None):
    print('quit')
    time.sleep(.1)


main()