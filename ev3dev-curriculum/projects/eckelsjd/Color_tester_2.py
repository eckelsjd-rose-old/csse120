import robot_controller as robo
import time


def main():

    print('Testing Colors:')
    robot = robo.Snatch3r()

    while True:
        print(robot.color_sensor.color)
        time.sleep(2)


main()
