"""Mario Kart PC controls: Displays a GUI which contains intructions on how
to drive the robot with the keyboard, (w=forward, a=left, d=right, space=use
powerup). The GUI will display images when the robot encounters certain
scenarios. GUI has a quit button that closes the mqtt connection and shuts
down the robot. Allows control of the robot with keyboard buttons."""

from tkinter import *
import mqtt_remote_method_calls as com
import time
import ev3dev.ev3 as ev3


class DataContainer(object):
    def __init__(self):
        self.current_powerup = 'None'
        self.photos = []
        self.window = None
        self.powerup_label = None
        self.star_ready = False
        self.mushroom_ready = False
        self.powerup_count = 0


class MyDelegate(object):
    """My Delegate on PC will display messages and images on PC letting user
    know that the robot has encountered certain scenarios in its terrain"""

    def __init__(self):
        self.running = True
        self.dc = DataContainer()

    def on_ink(self):
        change_photo(self, 3)

    def reset_photo(self):
        change_photo(self, 0)

    def on_star(self):
        print('on_star')
        time.sleep(1)
        set_powerup(self, 'star')
        change_photo(self, 1)
        print('after powerup')
        self.dc.powerup_count += 1
        self.dc.star_ready = True
        print(self.dc.powerup_count, self.dc.star_ready)

    def on_mushroom(self):
        print('on_mushroom')
        time.sleep(1)
        set_powerup(self, 'mushroom')
        change_photo(self, 1)
        self.dc.powerup_count += 1
        self.dc.mushroom_ready = True
        print(self.dc.powerup_count, self.dc.mushroom_ready)

    def close_window(self):
        self.running = False
        quit()


def main():
    """Creates a GUI and monitors the state of keyboard buttons to determine
        robot's motion."""

    my_delegate = MyDelegate()

    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root = Tk()
    root.title("Mario Kart")

    main_frame = Frame(root, width=400, height=400)
    main_frame.pack_propagate(0)
    main_frame.pack()

    picture_frame = Frame(main_frame, width=200, height=200,
                          background='white', borderwidth=4, relief=RIDGE)
    picture_frame.grid(columnspan=2, row=3, column=0)

    photo1 = PhotoImage(file='blank.gif')
    photo2 = PhotoImage(file='star_mario.gif')
    photo3 = PhotoImage(file='mushroom_.gif')
    photo4 = PhotoImage(file='ink.gif')
    # photo1 = 'white'
    # photo2 = 'yellow'
    # photo3 = 'red'
    # photo4 = 'black'
    my_delegate.dc.photos += [photo1, photo2, photo3, photo4]
    my_delegate.dc.window = Label(picture_frame, image=photo1)

    forward_button = Button(main_frame, text="Forward = w")
    forward_button["command"] = lambda: forward_callback(mqtt_client)
    forward_button.grid(row=0, column=1)
    root.bind('<w>', lambda event: forward_callback(mqtt_client))

    left_button = Button(main_frame, text="Left = a")
    left_button["command"] = lambda: left_callback(mqtt_client)
    left_button.grid(row=1, column=0)
    root.bind('<a>', lambda event: left_callback(mqtt_client))

    right_button = Button(main_frame, text="Right = d")
    right_button["command"] = lambda: right_callback(mqtt_client)
    right_button.grid(row=1, column=2)
    root.bind('<d>', lambda event: right_callback(mqtt_client))

    stop_button = Button(main_frame, text="Stop = s")
    stop_button["command"] = lambda: stop_callback(mqtt_client)
    stop_button.grid(row=1, column=1)
    root.bind('<s>', lambda event: stop_callback(mqtt_client))

    powerup_frame = Frame(main_frame, width=200, height=30,
                          background='yellow', borderwidth=6, relief=RAISED)
    powerup_frame.grid(columnspan=2, row=2, column=0)

    powerup_label = Label(powerup_frame, text="Powerup:")
    powerup_label.grid(row=0, column=0)

    my_delegate.dc.powerup_label = Label(powerup_frame,
                                         text=my_delegate.dc.current_powerup)
    my_delegate.dc.powerup_label.grid(row=0, column=1)

    use_powerup = Button(main_frame, text="Use Powerup = Space")
    use_powerup['command'] = lambda: powerup_callback(mqtt_client, my_delegate)
    use_powerup.grid(row=1, column=3)
    root.bind('<space>', lambda event: powerup_callback(mqtt_client,
                                                        my_delegate))

    quit_button = Button(main_frame, text="Quit")
    quit_button['command'] = lambda: quit_program(mqtt_client)
    quit_button.grid(row=3, column=3)
    root.bind('<q>', lambda event: quit_program(mqtt_client))

    root.bind('<KeyRelease-w>', lambda event: stop_callback(mqtt_client))
    root.bind('<KeyRelease-a>', lambda event: stop_callback(mqtt_client))
    root.bind('<KeyRelease-d>', lambda event: stop_callback(mqtt_client))

    root.mainloop()


def set_powerup(my_delegate, powerup):
    """Changes the powerup label on the GUI to the current powerup"""
    my_delegate.dc.powerup_label["text"] = powerup


def change_photo(my_delegate, k):
    """Changes the photo in the GUI to reflect the current scenario"""
    if k == 1:
        my_delegate.dc.window["image"] = my_delegate.dc.photos[1]
        my_delegate.dc.window.grid()
    if k == 2:
        my_delegate.dc.window["image"] = my_delegate.dc.photos[2]
        my_delegate.dc.window.grid()
    if k == 3:
        my_delegate.dc.window["image"] = my_delegate.dc.photos[3]
        my_delegate.dc.window.grid()
    else:
        my_delegate.dc.window["image"] = my_delegate.dc.photos[0]
        my_delegate.dc.window.grid()


def forward_callback(mqtt_client):
    """Calls robot to move forward on key press"""
    time.sleep(.1)
    mqtt_client.send_message("drive_forward")


def left_callback(mqtt_client):
    """Calls robot to turn left on key press"""
    time.sleep(.1)
    mqtt_client.send_message("turn_left")


def right_callback(mqtt_client):
    """Calls robot to turn right on key press"""
    time.sleep(.1)
    mqtt_client.send_message("turn_right")


def stop_callback(mqtt_client):
    time.sleep(.1)
    mqtt_client.send_message("stop")


def powerup_callback(mqtt_client, my_delegate):
    """Determines which powerup is currently possessed by the robot (up to
    1) and calls the robot to enact this powerup's function on key press"""
    print('powerup being called', my_delegate.dc.powerup_count)
    powerup_count = my_delegate.dc.powerup_count
    my_delegate.dc.powerup_count = 0
    set_powerup(my_delegate, 'None')

    if powerup_count == 1:

        if my_delegate.dc.star_ready:
            print('Before Star Thread')
            # threading.Thread(target=lambda: handle_star_gui(
            #     my_delegate)).start()
            my_delegate.dc.star_ready = False
            mqtt_client.send_message("use_star_powerup")

        if my_delegate.dc.mushroom_ready:
            # threading.Thread(target=lambda: handle_mushroom_gui(
            #     my_delegate)).start()
            my_delegate.dc.mushroom_ready = False
            mqtt_client.send_message("use_mushroom_powerup")


# def handle_star_gui(my_delegate):
#     """Changes Gui to reflect star powerup"""
#     change_photo(my_delegate, 1)
#     print('During star thread:', str(my_delegate.dc.window['image']))
#     time.sleep(5)
#     change_photo(my_delegate, 0)
#     set_powerup(my_delegate, 'None')
#     print('Finished Thread:', str(my_delegate.dc.window['image']))


# def handle_mushroom_gui(my_delegate):
#     """Changes Gui to reflect mushroom powerup"""
#     change_photo(my_delegate, 2)
#     print('During mushroom thread:')
#     time.sleep(5)
#     change_photo(my_delegate, 0)
#     set_powerup(my_delegate, 'None')
#     print('Finished Mushroom Thread')


def quit_program(mqtt_client):
    """Closes GUI and mqtt client, shuts down robot"""
    print("shutdown")
    mqtt_client.send_message("shutdown")
    exit()


def quit_window():
    print('Goodbye from Ev3')
    ev3.Sound.speak('Goodbye from E v 3')

    exit()


main()
