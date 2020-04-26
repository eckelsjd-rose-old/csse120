"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time
import random


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        """constructs Snatch3r object"""
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        assert self.left_motor.connected
        assert self.right_motor.connected

        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        assert self.arm_motor.connected

        self.touch_sensor = ev3.TouchSensor()
        assert self.touch_sensor.connected

        self.color_sensor = ev3.ColorSensor()
        assert self.color_sensor.connected

        self.ir_sensor = ev3.InfraredSensor()
        assert self.ir_sensor.connected

        self.beacon_seeker = ev3.BeaconSeeker(channel=1)

        self.pixy = ev3.Sensor(driver_name="pixy-lego")

        self.running = True

        self.mqtt_client = None

    def set_mqtt(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def drive_inches(self, distance, speed):
        """Drives robot a certain distance at a certain speed."""

        # Check that the motors are actually connected
        position = 90 * distance
        self.left_motor.run_to_rel_pos(speed_sp=speed, position_sp=position)
        self.right_motor.run_to_rel_pos(speed_sp=speed, position_sp=position)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, turn_degrees, turn_speed):
        """Turns the robot a certain amount of degrees at a certain speed."""
        # Left is positive

        position = (turn_degrees * 4.35)
        self.left_motor.run_to_rel_pos(speed_sp=turn_speed, position_sp=-position)
        self.right_motor.run_to_rel_pos(speed_sp=turn_speed, position_sp=position)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def arm_up(self):
        """Moves the robot arm up to top position."""
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.MediumMotor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()

    def arm_down(self):
        """Moves the robot arm down to the bottom position."""
        self.arm_motor.run_to_abs_pos(position_sp=0, speed_sp=900)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Blocks until the motor finishes running
        ev3.Sound.beep().wait()

    def arm_calibration(self):
        """Calibrates the robot arm."""
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.MediumMotor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()
        arm_revolutions_for_full_range = 14.2
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range * 360)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def shutdown(self):
        """Stops all arms, sets leds to green, and says goodbye."""
        self.running = False
        self.arm_motor.stop()
        self.right_motor.stop()
        self.left_motor.stop()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Sound.speak("Goodbye")
        print("Goodbye")

    def loop_forever(self):
        """Do nothing until MQTT calls shutdown"""
        while self.running:
            time.sleep(0.1)

    def drive(self, left_speed, right_speed):
        """Turns motors on at given speeds moving forward"""
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def drive_with_colors(self, left_speed, right_speed):
        self.drive(left_speed, right_speed)

        color = self.color_sensor.color
        if color == 5:  # Red
            self.mqtt_client.send_message("colors", [5])
        if color == 6:  # White
            self.mqtt_client.send_message("colors", [6])
        if color == 1:  # Black
            self.mqtt_client.send_message("colors", [1])

    def stop_motors(self):
        """Stops both motors"""
        self.left_motor.stop()
        self.right_motor.stop()

    def seek_beacon(self):
        """Will track and find a beacon object"""
        forward_speed = 300
        turn_speed = 50
        while True:
            current_heading = self.beacon_seeker.heading
            current_distance = self.beacon_seeker.distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                self.drive(turn_speed, -turn_speed)
            else:
                if math.fabs(current_heading) < 2:
                    # Close enough of a heading to move forward
                    print("On the right heading. Distance: ",
                          current_distance, current_heading)
                    if current_distance == 1:
                        time.sleep(0.6)
                        self.stop_motors()
                        return True
                    else:
                        self.drive(forward_speed, forward_speed)
                elif math.fabs(current_heading) >= 2 and math.fabs(
                        current_heading) < 10:
                    print('Current Heading: Check 1', current_heading)
                    if current_heading < 0:
                        print('Turning left')
                        self.drive(-turn_speed, turn_speed)
                    else:
                        print('Turning right')
                        self.drive(turn_speed, -turn_speed)
                else:
                    print('Heading too far off:', current_heading)
                    self.drive(-turn_speed, turn_speed)
            time.sleep(0.2)

    def spin_out(self):
        """Causes robot to turn a random amount of degrees at full speed"""
        degrees = random.randint(30, 360)
        self.turn_degrees(degrees, 900)
