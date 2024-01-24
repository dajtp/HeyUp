import configparser
import os
import shutil
import sys

print("Let's configure your HeyUp Client to be able to connect to your HeyUp Server.\n")

Server_IP = input("Please enter the IP address of your HeyUp Server: ")
Server_Port = input("Please enter the port number of your HeyUp Server: ")
HeyUp_User = input("Please enter the username of your HeyUp Server: ")
HeyUp_Pass = input("Please enter the password of your HeyUp Server: ")

config = configparser.ConfigParser()
config['SERVER_CREDS'] = {'Server_IP': Server_IP,
                    'Server_Port': Server_Port,
                    'Server_User': HeyUp_User,
                    'Server_Pass': HeyUp_Pass}

with open('HeyUpConfig.ini', 'w') as configfile:
    config.write(configfile)

print("\nYour HeyUp Client has been configured to connect to your HeyUp Server.")