# https://stackoverflow.com/questions/61607367/how-to-encrypt-json-in-python
# Working with JSON and cryptography

from cryptography.fernet import Fernet
import os.path
import json

data_swapnil = {'name': 'swapnil', 'age': 32, 'weight': 180, 'height': 175, 'location': 'mumbai' }
# data_trevor = {'name': 'trevor', 'age': 31, 'weight': 210, 'height': 185, 'location': 'austin' }
# data_julia = {'name': 'julia', 'age': 31, 'weight': 180, 'height': 175, 'location': 'austin' }

if os.path.isfile("symmetric_key.key"):
    print("Key file exists, using that")
    key_file = open("symmetric_key.key", 'rb')
    key_data = key_file.read()
    key_file.close()
else:
    print("Key file doesn't exist")
    key_data = Fernet.generate_key()
    key_file = open("symmetric_key.key",'wb')
    key_file.write(key_data)
    key_file.close()

fernet_obj = Fernet(key_data)

# Remember encrypt only takes bytes, so convert that str into bytes with .encode()
enc_swapnil_data = fernet_obj.encrypt(json.dumps(data_swapnil).encode())
print("swapnil_data: ", data_swapnil)
print("swapnil_data encoded into json: ", json.dumps(data_swapnil).encode())
print("enc_swapnil_data: ", enc_swapnil_data)

print("decrypted swapnil_data in dict format: ", json.loads(fernet_obj.decrypt(enc_swapnil_data)))


#############################################################################

# Alright so saving the private and public keys from RSA is a whole big deal
## - It's actually not - save_pkcs1 function inside rsa module - that's the one - save it as PEM
## - Going through the docs made me realize that
## Going through docs and learning how to program is the real deal of a software developer
## Understand how systems work - read the documentation - and then implement the system with programming
# using the RSA module doesn't seem to be the industry-way, everyone wants to use cryptography

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Okay - so these are really huge and involves a lot of rat-holing one day
# We're gonna have to figure out how much to rathole - where to rathole - how to figure out the use-cases
# How they are used in simple terms, how they are used in production - figure each one out completely

# On second thoughts - even RSA lib is powerful - and same goes for Crypto
# We need to figure out what needs to be done - signatures, hashing, signing, digests etc.
# How things are done in production
# And how to use the 3 libs - to accomplish those tasks - both in projects and in production - and how to save keys
# And how to transfer keys -
# At some point - even do that realpython tutorial on - HTTPS - where he builds a certificate authority server with Flask