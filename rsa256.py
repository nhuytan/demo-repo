from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_password(password, public_key):
    encrypted_password = public_key.encrypt(
        password.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_password


def decrypt_password(encrypted_password, private_key):
    decrypted_password = private_key.decrypt(
        encrypted_password,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode('utf-8')

    return decrypted_password


# Example usage
password = "mysecretpassword"

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()

# Encrypt the password
encrypted_password = encrypt_password(password, public_key)

# Decrypt the password
decrypted_password = decrypt_password(encrypted_password, private_key)

print("Original Password:", password)
print("Encrypted Password:", encrypted_password)
print("Decrypted Password:", decrypted_password)
