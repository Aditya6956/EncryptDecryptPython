# using the key
from cryptography.fernet import Fernet

with open('/home/aditya/encdec/filekey.key', 'rb') as filekey:
	key = filekey.read()

fernet = Fernet(key)

# opening the encrypted file
with open('/home/aditya/encdec/enc_file1.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('/home/aditya/encdec/dec_file1.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
