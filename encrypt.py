# opening the key
# import required module
from cryptography.fernet import Fernet

# # key generation
# key = Fernet.generate_key()

# # string the key in a file
# with open('/home/aditya/filekey.key', 'wb') as filekey:
#     filekey.write(key)

with open('/home/aditya/encdec/filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('/home/aditya/encdec/file1.csv', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('/home/aditya/encdec/enc_file1.csv', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
