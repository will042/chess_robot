import ur_socket_connection
from time import sleep

HOST = "192.168.56.101" # The remote host
PORT = 30001 # The same port as used by the server
s = ur_socket_connection.ur_socket_connection(HOST,PORT)

def coord2msg(x,y):
    z = 0.05
    rx = 0
    ry = 0
    rz = -3.14
    a = .5
    v = 0.2
    msg = "movel(p[" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(rx) + ", " + str(ry) + ", " + str(rz) + "], a=" + str(a) + ", v=" + str(v) + ")"
    print("Sent: ", msg)
    return msg

s.pass_msg(coord2msg(-0.2,-0.05))
