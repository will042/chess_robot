# Used to serve messages to the UR5
import socket
from time import sleep

class ur_socket_connection:

    def __init__(self, host, port):
        # self.host = host # The remote host
        # self.port = port # The same port as used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port)) # Bind to the port 
        print("Connection bound to: ", host, ":", str(port) )

    def pass_msg(self,msg):
        self.s.listen(5) # Now wait for client connection.
        print("Listening")
        self.c, self.addr = self.s.accept() # Establish connection with client.
        self.TCP = self.c.recv(1024)
        print("Current TCP: ", self.TCP)
        sleep(1)
        self.msg = msg
        self.encoded_msg = self.msg.encode('utf-8')
        print("Sending: ", self.encoded_msg)
        self.c.send(self.encoded_msg)
        print("Message Sent")

# c.close()
# s.close()
