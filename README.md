### Voice Controlled Chess Robot
![System Overview](https://raw.githubusercontent.com/will042/chess_robot/master/images/ChessRobot.png)

This is a project to develop a voice controlled chess robot. A Universal Robotics’ UR5e collaborative robot is used with a Robotiq Hand-E Gripper to manipulate chess pieces. A computer with Python 3.8, is used to accept voice commands, relay cartesian coordinates to the UR5e, and track the state of the board.


### Setup Instructions
* Download or clone
* `pip install requirements.txt`
* Set the location of the discard tray for chess pieces in `chess_movement_program.script`
* Copy the contents of `ur_programs` to the Teach Pendant
* Set the correct IP address for your computer in the `main_ur_loop` program on the Teach Pendant and in the `main_wakeword_version.py` or `main.py` files.

* Using the Teach Pendant, find the x-y coordinates of the a1 and h7 squares with respect to the base of the UR5e.
  ![Board Configuration](https://raw.githubusercontent.com/will042/chess_robot/master/images/BoardConfiguration.png)

* Set the a1 and h7 coordinates in `main_wakeword_version.py` or `main.py` as `cb = chess_board.chess_board(x0, y0, x7, y7)` 

### Usage
* Start by running the `main_ur_loop` on the Teach Pendant
* Run either `main.py` or `main_wakeword_version.py` to begin listening for voice input. The wakeword version listens for "robot" or "ok robot" using PocketSphinx. Movement commands are translated using the Google Speech Recognition API.
* During early development of this platform, the goal was to utilize standard algebraic chess notation for voice commands. It became clear that, in order for this to function correctly, it would require a bit of work developing a program capable of discerning words and letters that are easily misinterpreted by a speech recognition API e.g.: the letter “c” sounds quite similar to the letter “e.” Since this project’s goal is the realization of a feasibility prototype, it was decided to adapt a command grammar that could be more easily interpreted by a speech recognition API.

  Movement commands are given by stating two row-column pairs. An example of a move is shown below:
  
    ![Sample Move](https://raw.githubusercontent.com/will042/chess_robot/master/images/SampleMove.png)
