"""Mario Kart PC controls"""

from tkinter import *
import robot_controller as robo


class DataContainer(object):

    def __init__(self):
        self.contents = ' '
        self.photos = []
        self.window = None


def main():

    dc = DataContainer()

    robot = robo.Snatch3r

    root = Tk()
    root.title("Mario Kart")

    main_frame = Frame(root, width=400, height=400, background='white')
    main_frame.pack_propagate(0)
    main_frame.pack()

    picture_frame = Frame(main_frame, width=200, height=200,
                          background='gray')
    picture_frame.grid(columnspan=2, row=2, column=0)

    photo1 = PhotoImage(file='blank.gif')
    photo2 = PhotoImage(file='star_mario.gif')
    photo3 = PhotoImage(file='mushroom_.gif')
    photo4 = PhotoImage(file='ink.gif')
    dc.photos += [photo1, photo2, photo3, photo4]
    dc.window = Label(picture_frame, image=photo1)

    change = Button(main_frame, text='change photo')
    change['command'] = lambda: change_photo(dc)
    change.grid(row=6, column=0)

    change_color = Button(main_frame, text='change color')
    change_color['command'] = lambda: changecolor(robot)
    change_color.grid(row=5, column=3)

    forward_button = Label(main_frame, text="Forward = w")
    forward_button.grid(row=0, column=1)

    left_button = Label(main_frame, text="Left = a")
    left_button.grid(row=0, column=0)

    right_button = Label(main_frame, text="Right = d")
    right_button.grid(row=0, column=3)

    powerup_label = Label(main_frame, text="Powerup:")
    powerup_label.grid(row=1, column=0)

    powerup = Label(main_frame, text=dc.contents)
    powerup.grid(row=1, column=1)

    use_powerup = Label(main_frame, text="Use Powerup = Space")
    use_powerup.grid(row=1, column=3)

    quit_button = Button(main_frame, text="Quit")
    quit_button.grid(row=6, column=3)

    update_button = Button(main_frame, text='update')
    update_button['command'] = lambda: update(dc, powerup)
    update_button.grid(row=6, column=1)

    root.mainloop()


def update(dc, powerup):

    dc.contents = input("input: ")
    powerup["text"] = dc.contents


def change_photo(dc):

    k = int(input('number:'))
    if k == 0:
        dc.window['image'] = dc.photos[0]
        dc.window.grid()
    if k == 1:
        dc.window['image'] = dc.photos[1]
        dc.window.grid()
    if k == 2:
        dc.window['image'] = dc.photos[2]
        dc.window.grid()
    if k == 3:
        dc.window['image'] = dc.photos[3]
        dc.window.grid()


def changecolor(robot):
    print(robot.color_sensor.color)


main()