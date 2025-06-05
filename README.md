# Joystick Control Turtlesim

This is about to control turtlesim by using Arduino - Joystick setup. There will be a min-max values evaluation to finalize the value and then it will send to the `/cmd_vel` topic for action.

## How to make this work.

1. Clone the project.
2. Upload the arduino code to the arduino board (Select correct board type and port)
3. Use `ls /dev/tty*` to see all the ports or use arduino IDE for know the port.
4. Then modify the port in `joystick_teleop.py` file. Check below code snippet;
    ```
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Need to change port as per device
    ```
5. Then run `ros core`
6. Start turtlesim by `rosrun turtlesim turtlesim_node`
7. Run the node `rosrun joystick_control_turtlesim joystick_teleop.py`
8. Then able to see the Turtle move according to the joystick commands.

## Demostration Video
[![Demostratoion](https://img.youtube.com/vi/<id>/0.jpg)](https://www.youtube.com/watch?v=<id>)

<br>

_-Jayashanka Anushan_