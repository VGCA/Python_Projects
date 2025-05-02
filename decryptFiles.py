from cryptography.fernet import Fernet

key = Fernet.generate_key()
 
#with open('filekey.key', 'wb') as filekey:
#   filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
fernet = Fernet(key)

with open('file.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
decrypted = fernet.decrypt(encrypted)

with open('file.txt', 'wb') as dec_file:
    dec_file.write(decrypted)

print('Archivo desencriptado con éxito.')