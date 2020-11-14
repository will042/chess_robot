import ur_socket_connection
import chess_board
from time import sleep


# Initialize the socket object for communication with the teach pendant
HOST = "192.168.0.7" # The remote host
PORT = 8000 # The same port as used by the server
s = ur_socket_connection.ur_socket_connection(HOST,PORT)

# Initialize the chessboard. Specify the length of one side of the board.
# (x0, y0) gives the upper right corner of the board in the UR5 base coordinate system.
# Units are in meters.
cb = chess_board.chess_board(sidelength = 0.4, x0 = -0.6, y0 = -0.4)



# The generate_movestring function:
# Converts from Position 1 = Row1, Col1
#               Position 2 = Row2, Col2
# Where input = (Row1, Col1, Row2, Col2)
# To Cartesian coordinates in meters
# Also returns an indicator that states if the square that the piece needs
# to move to is occupied.
#
# Output is a string.
#
# output = "(occupied_indicator, x1, y1, x2, y2)"

x=cb.generate_movestring(0,1,0,3)
print(x)
s.pass_msg(x)  # Sends msg to UR5

