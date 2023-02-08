#!/usr/bin/env python3

######## Imports ########
import os, socket

try:
  from pyftpdlib.servers import FTPServer
except:
  os.system("pip3 install pyftpdlib==1.5.7")
finally:
  from pyftpdlib.handlers import FTPHandler
  from pyftpdlib.servers import FTPServer
  from pyftpdlib.authorizers import DummyAuthorizer
  from pyftpdlib.filesystems import UnixFilesystem


######## Global Variables ########
USR = "ftpuser"
PWD = "ftp"
PORT = 21
linPath = "/home/ftp"

######## Helper Function ########
def createFTPDirectory() -> None:
  if not os.path.exists(linPath):
    os.mkdir(linPath)

def runFTPServer() -> None:
  createFTPDirectory()
  authorizer = DummyAuthorizer()
  authorizer.add_user("c3t", "c3t",".", perm="elradfmwMT")

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.passive_ports = range(4445, 4450)
  
  # Define a customized banner (string returned when client connects)
  handler.banner = "pyftpdlib based ftpd ready."
  
  server = FTPServer(('', PORT), handler)

  server.max_cons = 256
  server.max_cons_per_ip = 5

  server.serve_forever()


if __name__ == '__main__':
  runFTPServer()
