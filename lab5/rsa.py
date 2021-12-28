from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)
token = f.encrypt(b"I like ice cream")
print(f'\nEncrypted message: {token}')

decrypted = f.decrypt(token)
print(f'Decrypted message: {decrypted}\n')
