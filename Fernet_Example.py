from cryptography.fernet import Fernet

Key = Fernet.generate_key()
print(Key)

Key1 = Fernet(Key)
print(Key1)

Input_Msg = input("What's The Message: ")
Input_Msg_Enc = Input_Msg.encode("utf-8")

Token_Message = Key1.encrypt(Input_Msg_Enc)
print(Token_Message)

Dec_Token_Msg = Key1.decrypt(Token_Message)
print(Dec_Token_Msg)

