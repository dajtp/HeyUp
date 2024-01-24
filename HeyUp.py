# This is the main file for the HeyUp application. This script will contain and run the main function of our application. 
# I will create seperate files for the other functions of the application - i.e. the encryption and decryption functions, key generation and management and all network/server functions.


# Importing the required external libraries.
import cryptography
#from Crypto.Hash import *
import os
import shutil
import argparse
import socket
import sys
import time
import datetime
import threading
import configparser

# Importing from internal Python Scripts.

#import Fernet_Example
#import Build_Config

config = configparser.ConfigParser()
config.read('HeyUpConfig.ini')

Server_IP = config['IP']['Server_IP']
Server_Port = config['PORT']['Server_Port']

print(Server_IP)
print(Server_Port)




