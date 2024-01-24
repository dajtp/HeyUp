import configparser
import os
import shutil
import sys

print("Let's configure your HeyUp Client to be able to connect to your HeyUp Server.\n")

Server_IP = input("Please enter the IP address of your HeyUp Server: ")
Server_Port = input("Please enter the port number of your HeyUp Server: ")

config = configparser.ConfigParser()
config['IP'] = {'Server_IP': Server_IP}
config['PORT'] = {'Server_Port': Server_Port}

with open('HeyUpConfig.ini', 'w') as configfile:
    config.write(configfile)

print("\nYour HeyUp Client has been configured to connect to your HeyUp Server.")