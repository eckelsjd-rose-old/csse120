#######
# Name: Joshua Key
# Theme: Rage Game
#
#
#
#######

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import random
import time


class MyDelegate(object):
    def __init__(self):
        self.speed = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        self.count = 0
        self.color = None

    def colors(self, color):
        self.color = color


def main():

    delegate = MyDelegate()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Rage")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    easy = tkinter.IntVar()
    easy_mode = ttk.Checkbutton(main_frame, text="Easy Mode", variable=easy)
    easy_mode.grid(row=7, column=2)

    progress_variable = tkinter.IntVar()
    progress = ttk.Progressbar(main_frame, mode='determinate', variable=progress_variable)
    progress.grid(row=11, column=2)
    progress_label = ttk.Label(main_frame, text="Progress")
    progress_label.grid(row=10, column=2)

    set_up_1(root, main_frame, mqtt_client, delegate, easy, progress_variable)

    root.mainloop()


def set_up_1(root, main_frame, mqtt_client, delegate, easy, progress):

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<w>', lambda event: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: left_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<a>', lambda event: left_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: right_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<d>', lambda event: right_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: back_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<s>', lambda event: back_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    win_button = ttk.Button(main_frame, text="Win")
    win_button.grid(row=5, column=1)
    win_button['command'] = lambda: win_callback(progress, mqtt_client)
    root.bind('b', lambda event: win_callback(progress, mqtt_client))

    gamble_button = ttk.Button(main_frame, text="Gamble")
    gamble_button.grid(row=6, column=2)
    gamble_button['command'] = lambda: gamble(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<g>', lambda event: gamble(root, main_frame, mqtt_client, delegate, easy, progress))
    root.bind('<KeyRelease>', lambda event: stop_callback(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=10, column=0)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=11, column=0)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def set_up_2(root, main_frame, mqtt_client, delegate, easy, progress):
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: gamble(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<w>', lambda event: gamble(root, main_frame, mqtt_client, delegate, easy, progress))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<a>', lambda event: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: left_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<d>', lambda event: left_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: right_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<s>', lambda event: right_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    win_button = ttk.Button(main_frame, text="Win")
    win_button.grid(row=5, column=1)
    win_button['command'] = lambda: back_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('b', lambda event: back_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    gamble_button = ttk.Button(main_frame, text="Gamble")
    gamble_button.grid(row=6, column=2)
    gamble_button['command'] = lambda: win_callback(mqtt_client, progress)
    root.bind('<g>', lambda event: win_callback(mqtt_client, progress))
    root.bind('<KeyRelease>', lambda event: stop_callback(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=10, column=0)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=11, column=0)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def set_up_3(root, main_frame, mqtt_client, delegate, easy, progress):
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: win_callback(main_frame, progress)
    root.bind('<w>', lambda event: win_callback(main_frame, progress))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: gamble(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<a>', lambda event: gamble(root, main_frame, mqtt_client, delegate, easy, progress))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<d>', lambda event: forward_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: left_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<s>', lambda event: left_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    win_button = ttk.Button(main_frame, text="Win")
    win_button.grid(row=5, column=1)
    win_button['command'] = lambda: right_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('b', lambda event: right_callback(root, main_frame, mqtt_client, delegate, easy, progress))

    gamble_button = ttk.Button(main_frame, text="Gamble")
    gamble_button.grid(row=6, column=2)
    gamble_button['command'] = lambda: back_callback(root, main_frame, mqtt_client, delegate, easy, progress)
    root.bind('<g>', lambda event: back_callback(root, main_frame, mqtt_client, delegate, easy, progress))
    root.bind('<KeyRelease>', lambda event: stop_callback(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=10, column=0)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=11, column=0)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def forward_callback(root, main_frame, mqtt_client, delegate, easy, progress):
    time.sleep(0.5)
    print('Forward')
    speed = 500
    delegate.count = random.randrange(10)
    if easy == 0:
        speed = delegate.speed[random.randrange(9)]
        if delegate.count == 0:
            ev3.Sound.beep()
            set_up_1(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 3:
            ev3.Sound.beep()
            set_up_2(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 6:
            ev3.Sound.beep()
            set_up_3(root, main_frame, mqtt_client, delegate, easy, progress)

    mqtt_client.send_message("drive_with_colors", [speed, speed])

    if delegate.color == 5:  # Red
        progress.set(progress.get() + 7)
    if delegate.color == 6:  # White
        progress.set(progress.get() + 5)
    if delegate.color == 1:  # Black
        progress.set(progress.get() + 10)


def left_callback(root, main_frame, mqtt_client, delegate, easy, progress):
    time.sleep(0.5)
    print('Left')
    speed = 500
    delegate.count = random.randrange(10)
    if easy == 0:
        speed = delegate.speed[random.randrange(9)]
        if delegate.count == 0:
            ev3.Sound.beep()
            set_up_1(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 3:
            ev3.Sound.beep()
            set_up_2(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 6:
            ev3.Sound.beep()
            set_up_3(root, main_frame, mqtt_client, delegate, easy, progress)

    mqtt_client.send_message("drive_with_colors", [-speed, speed])

    if delegate.color == 5:  # Red
        progress.set(progress.get() + 7)
    if delegate.color == 6:  # White
        progress.set(progress.get() + 5)
    if delegate.color == 1:  # Black
        progress.set(progress.get() + 10)


def stop_callback(mqtt_client):
    print('Stop')
    mqtt_client.send_message("stop_motors")


def right_callback(root, main_frame, mqtt_client, delegate, easy, progress):
    time.sleep(0.5)
    print('Right')
    speed = 500
    delegate.count = random.randrange(10)
    if easy == 0:
        speed = delegate.speed[random.randrange(9)]
        if delegate.count == 0:
            ev3.Sound.beep()
            set_up_1(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 3:
            ev3.Sound.beep()
            set_up_2(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 6:
            ev3.Sound.beep()
            set_up_3(root, main_frame, mqtt_client, delegate, easy, progress)

    mqtt_client.send_message("drive_with_colors", [speed, -speed])

    if delegate.color == 5:  # Red
        progress.set(progress.get() + 7)
    if delegate.color == 6:  # White
        progress.set(progress.get() + 5)
    if delegate.color == 1:  # Black
        progress.set(progress.get() + 10)


def back_callback(root, main_frame, mqtt_client, delegate, easy, progress):
    time.sleep(0.5)
    print('Back')
    delegate.count = random.randrange(10)
    speed = 500
    if easy == 0:
        speed = delegate.speed[random.randrange(9)]
        if delegate.count == 0:
            ev3.Sound.beep()
            set_up_1(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 3:
            ev3.Sound.beep()
            set_up_2(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 6:
            ev3.Sound.beep()
            set_up_3(root, main_frame, mqtt_client, delegate, easy, progress)

    mqtt_client.send_message("drive_with_colors", [-speed, -speed])

    if delegate.color == 5:  # Red
        progress.set(progress.get() + 7)
    if delegate.color == 6:  # White
        progress.set(progress.get() + 5)
    if delegate.color == 1:  # Black
        progress.set(progress.get() + 10)


def gamble(root, main_frame, mqtt_client, delegate, easy, progress):
    delegate.count = random.randrange(4)
    progress.set(progress.get() + random.randrange(10))
    if easy == 0:
        if delegate.count == 0:
            ev3.Sound.beep()
            set_up_1(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 3:
            ev3.Sound.beep()
            set_up_2(root, main_frame, mqtt_client, delegate, easy, progress)
        if delegate.count == 6:
            ev3.Sound.beep()
            set_up_3(root, main_frame, mqtt_client, delegate, easy, progress)


def win_callback(progress, mqtt_client):
    if progress.get() >= 90:
        print("You Win!")
        mqtt_client.send_message("stop_motors")
        quit_program(mqtt_client, True)
    else:
        main()


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()
