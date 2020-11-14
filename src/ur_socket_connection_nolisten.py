# URScript Raw Transmission Object
# For sending messages directly to the UR5
# One way communication, no handshake
# Will stop any programs running on teach pendant

class ur_socket_connection:

    def __init__(self, host, port):
        import socket
        self.host = host # The remote host
        self.port = port # The same port as used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

    def pass_msg(self,msg):

        self.s.send ((msg + "\n").encode('utf8'))
        self.data = self.s.recv(1024)
        print ("Received: ", ((self.data)))

    def close_socket(self):

        self.s.close()
