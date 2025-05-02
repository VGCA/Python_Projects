from cryptography.fernet import Fernet

key = Fernet.generate_key()
 
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
fernet = Fernet(key)

with open('file.txt', 'rb') as file:
    original = file.read()
     
encrypted = fernet.encrypt(original)
 
with open('file.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

print(f'Archivo encriptado con éxito. Creada llave para desencriptar')