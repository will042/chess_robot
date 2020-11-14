# Used to serve messages to the UR5

import socket
import time
import urlib as ur

HOST = "192.168.0.7" # The remote host
PORT = 8000 # The same port as used by the server

print("Opening Socket")
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT)) # Bind to the port 
s.listen(5) # Now wait for client connection.
print("Listening")
c, addr = s.accept() # Establish connection with client.

msg = c.recv(1024)
print("Current TCP: ", msg)
time.sleep(1)

send_msg = "(1, -0.3, -0.2, -0.3, -0.5)"
send_msg = send_msg.encode('utf-8')
print("Sending: ", send_msg)
c.send(send_msg)


# c.close()
# s.close()

print("Message Sent")

# movej([0,-3.1415/2, 3.1415/2, -3.1415/2, -3.1415/2, 0])