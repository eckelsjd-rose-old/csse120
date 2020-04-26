"""Mario Kart ev3: Handles robot motion callbacks, and calls them on the
ev3.Snatch3r robot. Calls functions on PC to display images and labels when
certain objects are encountered. Changes speed and actions of robot based on
color sensor readings."""

import robot_controller as robo
import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com
import threading


class DataContainer(object):
    def __init__(self):
        self.left_speed = 400
        self.right_speed = 400
        self.on_road = True
        self.powerup_mode = False
        self.star_mode = False
        self.starting_speed = 0
        self.available = [True, True]


class MyDelegate(object):
    """My Delegate on ev3 will receive controls from the PC on when to
    drive, shutdown, and use powerups"""

    def __init__(self):
        self.running = True
        self.robot = robo.Snatch3r()
        self.dc = DataContainer()

    def reset_drive(self):
        self.robot.drive(self.dc.left_speed, self.dc.right_speed)

    def drive_forward(self):
        self.dc.starting_speed = 1
        self.robot.drive(self.dc.left_speed, self.dc.right_speed)

    def turn_left(self):
        self.robot.drive(-self.dc.left_speed, self.dc.right_speed)

    def turn_right(self):
        self.robot.drive(self.dc.left_speed, -self.dc.right_speed)

    def stop(self):
        self.dc.starting_speed = 0
        self.robot.stop_motors()

    def shutdown(self):
        self.robot.shutdown()
        self.running = False

    def use_star_powerup(self):
        self.dc.available[0] = True
        threading.Thread(target=lambda: inact_star(self, 700, 700,
                                                   5)).start()

    def use_mushroom_powerup(self):
        self.dc.available[1] = True
        threading.Thread(target=lambda: inact_mushroom(self, 700, 700,
                                                       5)).start()


def main():
    """Constantly monitors the color sensor of the robot, and calls
    functions accordingly. Robot is being controlled by getch() method from
    PC keyboard."""

    print('hello')
    threading.Thread(target=lambda: play_song()).start()
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_pc()

    while my_delegate.running:

        #black = my_delegate.robot.color_sensor.COLOR_BLACK
        blue = my_delegate.robot.color_sensor.COLOR_BLUE
        yellow = my_delegate.robot.color_sensor.COLOR_YELLOW
        red = my_delegate.robot.color_sensor.COLOR_RED
        brown = my_delegate.robot.color_sensor.COLOR_BROWN
        white = my_delegate.robot.color_sensor.COLOR_WHITE

        color = my_delegate.robot.color_sensor.color

        touch_button = my_delegate.robot.touch_sensor

        if color != white:

            if color == brown:
                my_delegate.robot.spin_out()
                mqtt_client.send_message("on_ink")
                threading.Thread(target=lambda: inact_ink(mqtt_client,
                                                          5)).start()

            if color == blue:
                print('Blue 1')
                threading.Thread(target=lambda: inact_speed_boost(my_delegate,
                                                                  700,
                                                                  700)).start()

            if my_delegate.dc.available[0] and color == yellow:
                print('Found yellow')
                my_delegate.dc.available[0] = False
                mqtt_client.send_message("on_star")
                threading.Thread(target=lambda: inact_star_gui(mqtt_client)).start()

            if my_delegate.dc.available[1] and color == red:
                print('Found red')
                my_delegate.dc.available[1] = False
                mqtt_client.send_message("on_mushroom")
                threading.Thread(target=lambda: inact_mushroom_gui(
                    mqtt_client)).start()

            my_delegate.dc.on_road = True

            if not my_delegate.dc.powerup_mode:  # Robot is on road w/o powerup
                if my_delegate.dc.starting_speed == 0:  # Robot is not moving
                    # (holding still) while on road
                    my_delegate.dc.left_speed = 400
                    my_delegate.dc.right_speed = 400
                else:  # Robot is already moving on road
                    my_delegate.dc.left_speed = 400
                    my_delegate.dc.right_speed = 400
                    my_delegate.reset_drive()

        else:
            if not my_delegate.dc.star_mode:  # Robot is off road w/o star
                if my_delegate.dc.starting_speed == 0:  # Robot is not moving
                    #  while off road (holding still)
                    my_delegate.dc.left_speed = 200
                    my_delegate.dc.right_speed = 200
                    my_delegate.dc.on_road = False
                else:  # Robot is already moving while off road
                    my_delegate.dc.left_speed = 200
                    my_delegate.dc.right_speed = 200
                    my_delegate.reset_drive()
                    my_delegate.dc.on_road = False

        if touch_button.is_pressed:
            break

        time.sleep(.01)

    mqtt_client.send_message("close_window")
    ev3.Sound.speak('Goodbye')
    exit()


def inact_star(my_delegate, left_speed, right_speed, length):
    """Activates star powerup for a given length of time (5 seconds),
    then returns conditions to normal"""
    my_delegate.dc.powerup_mode = True
    my_delegate.dc.star_mode = True
    my_delegate.dc.left_speed = left_speed
    my_delegate.dc.right_speed = right_speed
    my_delegate.reset_drive()

    time.sleep(length)

    my_delegate.dc.left_speed = 400
    my_delegate.dc.right_speed = 400
    my_delegate.dc.powerup_mode = False
    my_delegate.dc.star_mode = False
    my_delegate.reset_drive()


def inact_mushroom(my_delegate, left_speed, right_speed, length):
    """Activates mushroom powerup for a given length of time (5 seconds),
    then returns the conditions to normal"""
    my_delegate.dc.powerup_mode = True
    my_delegate.dc.left_speed = left_speed
    my_delegate.dc.right_speed = right_speed
    my_delegate.reset_drive()

    time.sleep(length)

    my_delegate.dc.left_speed = 400
    my_delegate.dc.right_speed = 400
    my_delegate.dc.powerup_mode = False
    my_delegate.reset_drive()


def inact_star_gui(mqtt_client):
    time.sleep(5)
    mqtt_client.send_message("reset_photo")


def inact_mushroom_gui(mqtt_client):
    time.sleep(5)
    mqtt_client.send_message("reset_photo")


def inact_ink(mqtt_client, t):
    """Activates the condition in which the player has been 'inked' for a
    given length of time, then returns conditions to normal"""
    time.sleep(t)
    mqtt_client.send_message('reset_photo')


def inact_speed_boost(my_delegate, left_speed, right_speed):
    """Activates a speed boost for a given length of time (5 seconds) when
    kart runs over a 'speed boost', then returns speed to normal."""
    print('THREAD IS HAPPENING')
    my_delegate.dc.powerup_mode = True
    my_delegate.dc.left_speed = left_speed
    my_delegate.dc.right_speed = right_speed
    my_delegate.reset_drive()

    time.sleep(3)
    print("THREAD HAS ENDED")
    my_delegate.dc.left_speed = 400
    my_delegate.dc.right_speed = 400
    my_delegate.dc.powerup_mode = False
    my_delegate.reset_drive()


def play_song():
    volume = ev3.Sound.get_volume()
    print(volume)
    ev3.Sound.set_volume(500)
    ev3.Sound.play("mario_08.wav")


main()
