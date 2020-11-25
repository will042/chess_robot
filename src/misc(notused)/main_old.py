import ur_socket_connection
import chess_board
from time import sleep


# Initialize the socket object for communication with the teach pendant
HOST = "192.168.0.12" # The remote host
PORT = 8000 # The same port as used by the server
s = ur_socket_connection.ur_socket_connection(HOST,PORT)

# Initialize the chessboard. Specify the length of one side of the board.
# (x0, y0) gives the upper left corner of the board in the UR5 base coordinate system.
# Units are in meters.
# cb = chess_board.chess_board(x0 = 0.330, y0 = -0.8, x7 = 0.010, y7 = -0.430)
# cb = chess_board.chess_board(x0 = 0.12950, y0 = -0.44720, x7 = -0.13589, y7 = -0.71350)

cb = chess_board.chess_board(x0 = 0.24014, y0 = -0.46005, x7 = -.02449, y7 = -0.72676)

# A8=(0,0)=(y0,x0) ...  ... H8=(0,7)
#    .                          .
#    .                          .
# A1=(7,0)          ...  ... H1=(7,7)=(y7,x7)
# The generate_movestring function:
# Converts from Position 1 = Row1, Col1
#               Position 2 = Row2, Col2
# Where input = (Row1, Col1, Row2, Col2) (y1,x1,y2,x2)
# To Cartesian coordinates in meters
# Also returns an indicator that states if the square that the piece needs
# to move to is occupied.
#
# Output is a string.
#
# output = "(occupied_indicator, x1, y1, x2, y2)"

x=cb.generate_movestring_alt(1,0,0,4,0) #In Row,Col notation
print(x)
s.pass_msg(x)  # Sends msg to UR5

#330,-800 top left, a8
#10,-430 bottom right, h1