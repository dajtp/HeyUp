# This is the main file for the HeyUp application. This script will contain and run the main function of our application. 
# I will create seperate files for the other functions of the application - i.e. the encryption and decryption functions, key generation and management and all network/server functions.


# Importing the required external libraries.
import cryptography
import os
import shutil
import argparse
import socket
import sys
import time
import datetime
import threading

# Importing from internal Python Scripts.

import Fernet_Example
