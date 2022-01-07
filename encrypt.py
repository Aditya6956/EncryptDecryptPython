import os
from kafka import KafkaProducer
from cryptography.fernet import Fernet

# # key generation
# key = Fernet.generate_key()

# # string the key in a file
# with open('/home/aditya/filekey.key', 'wb') as filekey:
#     filekey.write(key)

topic_name = 'encrypt'
producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('/home/aditya/encdec/filekey.key', 'rb') as filekey:
	key = filekey.read()

fernet = Fernet(key)

with open('/home/aditya/encdec/HealthCare.csv', 'rb') as file:
	original = file.read()
	
encrypted = fernet.encrypt(original)

with open('/home/aditya/encdec/enc_HealthCare.csv', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

with open('/home/aditya/encdec/enc_HealthCare.csv', 'rb') as encrypted_file:
    data = encrypted_file.read()
    producer.send(topic_name, data)
