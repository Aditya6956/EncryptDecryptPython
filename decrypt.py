# using the key
from cryptography.fernet import Fernet

with open('/home/aditya/encdec/filekey.key', 'rb') as filekey:
	key = filekey.read()

fernet = Fernet(key)

with open('/home/aditya/encdec/enc_HealthCare.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('/home/aditya/encdec/dec_HealthCare.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
