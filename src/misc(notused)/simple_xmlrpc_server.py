# XMLRPC server
# Based off of: https://www.universal-robots.com/articles/ur/xml-rpc-communication/

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import numpy as np
import urlib as ur

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.7', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def position():

        return position

    server.register_function(position, 'position')

    
    server.serve_forever()
