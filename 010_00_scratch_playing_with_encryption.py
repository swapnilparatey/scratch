## https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
## Incase you're wanting to get depressed later - https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
## Mind-numbing article - but the XOR encryption seems promising
## Also - the article above from tutorialspoint is boring and old.

## Symmetric key encryption with cryptography
#from cryptography.fernet import Fernet

## Asymmetric key encryption with - this module is not used in the world a lot
## - the cryptography module has a lot of rsa bindings - so cryptography is used instead
import rsa


## Symmetric key encryption with cryptography - just one key - less secure - susceptible to middle men attacks
## Whoever has the key - can read the messages
# message = "hello geeks"
# key = Fernet.generate_key()
# fernet = Fernet(key)
# encMessage = fernet.encrypt(message.encode())
# print("original string: ", message)
# print("encrypted string: ", encMessage)
# decMessage = fernet.decrypt(encMessage).decode()
# print("decrypted message: ", decMessage)


## Public and private key - asymmetric encryption - RSA stuff - private and public keys are objects
publicKey, privateKey = rsa.newkeys(512)
message = "suck a bag of fruit snacks"
encMessage = rsa.encrypt(message.encode(), publicKey)
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print(decMessage)