#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import serial

def map_range(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def main():
    rospy.init_node('joystick_teleop')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(20)

    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Adjust port if needed
    move_cmd = Twist()

    while not rospy.is_shutdown():
        try:
            line = arduino.readline().decode('utf-8').strip()
            if not line:
                continue

            parts = line.split('\t')
            if len(parts) != 3:
                continue

            x_raw = int(parts[0])
            y_raw = int(parts[1])
            button = int(parts[2])

            linear = map_range(y_raw, 0, 1023, 1.5, -1.5)
            angular = map_range(x_raw, 0, 1023, 2.0, -2.0)

            deadzone = 50
            move_cmd.linear.x = linear if abs(y_raw - 512) > deadzone else 0
            move_cmd.angular.z = angular if abs(x_raw - 512) > deadzone else 0

            pub.publish(move_cmd)

        except Exception as e:
            rospy.logwarn(f"Error reading joystick: {e}")
            continue

        rate.sleep()

if __name__ == '__main__':
    main()
