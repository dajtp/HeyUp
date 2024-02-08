# This is the main file for the HeyUp application. This script will contain and run the main function of our application. 
# I will create seperate files for the other functions of the application - i.e. the encryption and decryption functions, key generation and management and all network/server functions.


# Importing the required external libraries.
import cryptography
#from Crypto.Hash import *
import os
import shutil
import argparse
import sys
import time
import datetime
import threading
import configparser
from tcppinglib import tcpping
import socket

# Importing from internal Python Scripts.

#import Fernet_Example
#import Build_Config

config = configparser.ConfigParser()
config.read('HeyUpConfig.ini')

Server_IP = config['SERVER_CREDS']['Server_IP']
Server_Port = config['SERVER_CREDS']['Server_Port']
HeyUp_User = config['SERVER_CREDS']['Server_User']
HeyUp_Pass = config['SERVER_CREDS']['Server_Pass']

# Ping Server
def pingserver():
    Host = tcpping(Server_IP, Server_Port, 2, 3, 0.1)
    if Host.is_alive == True:
        print("Server is up and running.")
        pass
    else:
        print("Server is down. Exiting application.")
        sys.exit()

# Receive Messages
def recvmsg():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (Server_IP, Server_Port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        message = 'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()

pingserver()

