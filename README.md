### Voice Controlled Chess Robot
![System Overview](https://raw.githubusercontent.com/will042/chess_robot/master/images/ChessRobot.png)

This is a project to develop a voice controlled chess robot. A Universal Robotics’ UR5e collaborative robot is used with a Robotiq Hand-E Gripper to manipulate chess pieces. A computer with Python 3.8, is used to accept voice commands, relay cartesian coordinates to the UR5e, and track the state of the board. [Python Chess](https://github.com/niklasf/python-chess) is used for tracking the state of the board and [Speech Recognition](https://github.com/Uberi/speech_recognition) is used for translating voice commands.


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
  
  ![Sample Move](https://raw.githubusercontent.com/will042/chess_robot/master/images/Sample_Move.png)

  The full terminal output:
  
  ![Terminal Output](https://raw.githubusercontent.com/will042/chess_robot/master/images/TerminalOutput.png)
  
### How it Works:
  
  ![ProcessFlow](https://raw.githubusercontent.com/will042/chess_robot/master/images/ProcessFlowDiagram.png)
  
  
### Goals for Improvement:

* Integrate a chess engine using [Python Chess's](https://github.com/niklasf/python-chess) support for UCI engine communication.
* Improve speech recognition so that moves can be specified in standard algebraic notation.
* Improve accuracy of gripper Z-position by keeping track of the height of each piece on the board. As of now, all pieces are assumed to be the same height.
* Integrate machine vision for more accurate targeting of chess pieces.
