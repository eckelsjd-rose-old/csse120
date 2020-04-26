#######
# Name: Joshua Key
# Theme: Rage Game
#
#
#
#######

import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def main():
    """Run final project"""
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    robot.set_mqtt(mqtt_client)
    mqtt_client.connect_to_pc()
    robot.loop_forever()


main()
