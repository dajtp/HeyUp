# This script's sole function is to create and store the encryption keys used by the application.

from Crypto.PublicKey import RSA

print("Generating Keys...")
Input = input("Please Enter a Secure Passphrase: ")
Secret_Code = str(Input)
Key = RSA.generate(2048)
Encrypted_Key = Key.exportKey(passphrase=Secret_Code, pkcs=8, protection="scryptAndAES128-CBC")

with open("private.pem", "wb") as f:
    f.write(Encrypted_Key)  # This is the private key. Keep it safe!
    f.close()

with open("public.pem", "wb") as f:
    f.write(Key.publickey().exportKey())
    f.close()

Show = input("Would you like to see the keys? (Y/N): ")
if Show == 'Y' or Show == 'y':
    print(Key.publickey().exportKey())
    print("\n\n")
    print(Encrypted_Key)
else:
    print("Keys Generated Successfully!!")

