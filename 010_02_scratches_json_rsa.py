import rsa
import os.path

nbits = 2048

if os.path.isfile("rsa_public_key.pem"):
    print("file exists - using that one")
    # Loading the public key file
    publicKey = rsa.PublicKey.load_pkcs1(open("rsa_public_key.pem",'rb').read(),format='PEM')
    # Doing the same for the private key file - loading it
    privateKey = rsa.PrivateKey.load_pkcs1(open("rsa_private_key.pem",'rb').read(),format='PEM')
else:
    print("Public and private keys not found ... creating them")
    publicKey, privateKey = rsa.newkeys(nbits)  # Create public and private keys coz you didn't find them

    with open("rsa_public_key.pem",'wb') as public_key_file:
        public_key_file.write(publicKey.save_pkcs1(format='PEM'))
        public_key_file.close()     # Save the public key

    with open("rsa_private_key.pem",'wb') as private_key_file:
        private_key_file.write(privateKey.save_pkcs1(format='PEM'))
        private_key_file.close()    # Save the private key


print("private key: ", privateKey.save_pkcs1(format='PEM'))
print("\n\npublic key: ", publicKey.save_pkcs1(format='PEM'))

message = "what the fuck are you sending... then does this increase to more than 53.... "
# WTF why is the message limited to only 53 bytes?
# It's because of that newkey(arg) = if you put 512 in it, then the max message bytes is 64-11 = 53
# If you put 1024 in it - then it becomes 117
# If you put 2048 in it - then max becomes 245
# If you put 4096 in it - then it becomes 501

try:
    encMessage = rsa.encrypt(message.encode(),publicKey)
    print("\n\nEncrypted message: ", encMessage)
    print("\n\nOriginal message:", message)
    decMessage = rsa.decrypt(encMessage, privateKey).decode()
except OverflowError:
    print("Message length exceeded depending on your public key nbits")

# Decided to not give a care about json here - because of course we're assuming it works