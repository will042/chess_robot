### Voice Controlled Chess Robot
![System Overview](https://raw.githubusercontent.com/will042/chess_robot/master/images/ChessRobot.png)

This is a project to develop a voice controlled chess robot. A Universal Robotics’ UR5e collaborative robot is used with a Robotiq Hand-E Gripper to manipulate chess pieces. A computer with Python 3.8, is used to accept voice commands, interpret and relay cartesian coordinates to the UR5e, and track the state of the chess game.


### Setup Instructions
* Download or clone
* `pip install requirements.txt`
* Set the location of the discard tray for chess pieces in `chess_movement_program.script`
* Copy the contents of `ur_programs` to the Teach Pendant
* Set the correct IP address for your computer in the `main_ur_loop` program on the Teach Pendant
* 
