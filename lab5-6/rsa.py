from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Generate a public key
public_key = private_key.public_key()

message = b"I like ice cream"
#Encrypt message with public key
encrypted = public_key.encrypt(message, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))

#Decrypt message with private key
decrypted = private_key.decrypt(encrypted, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))

print(f'\nOriginal message: {message}')
print(f'\nMessage encrypted with public key: {encrypted}')
print(f'\nMessage decrypted with private key: {decrypted}\n')
