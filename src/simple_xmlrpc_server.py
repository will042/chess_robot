# XMLRPC server
# Based off of: https://www.universal-robots.com/articles/ur/xml-rpc-communication/

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import numpy as np
import urlib as ur

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.7', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def actioncheck():
        
        # 0 = idle
        # 1 = move
        # 2 = close grip
        # 3 = open grip

        return actionnumber

    server.register_function(action, 'action')



    def position():

        #get the pose here

        return pose

    server.register_function(position, 'position')





    # class chess_board:

    #     def classtest(self):

    #         return ur.listToPose([-0.2, -0.5, 0.5, 0, 0, -3.14])

    # server.register_instance(chess_board(8,0,0))





    # Run the server's main loop
    server.serve_forever()