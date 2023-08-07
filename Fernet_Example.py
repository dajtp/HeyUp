from cryptography.fernet import Fernet
import os
import socket
import shutil


Key = Fernet.generate_key()
#print(Key)

Key1 = Fernet(Key)
#print(Key1)

with open("TheSecretKey.txt", "w") as f:
    f.write(str(Key))
    f.close
    
Key_Location = input("Where would you like to safely store your private key?: ")
shutil.move('TheSecretKey.txt', Key_Location)

Input_Msg = input("What's The Message: ")
Input_Msg_Enc = Input_Msg.encode("utf-8")

Token_Message = Key1.encrypt(Input_Msg_Enc)
print(Token_Message)

Message_Location = input("Where would you like to store your encrypted message?: ")
enc_token_file = open(str(Message_Location) + "/" + "Encrypted_Msg.txt", "w")
enc_token_file.write(str(Token_Message))
enc_token_file.close

Dec_Token_Msg = Key1.decrypt(Token_Message)
print(Dec_Token_Msg)

