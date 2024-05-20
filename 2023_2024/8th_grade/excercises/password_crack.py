import base64
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

####################################################################################################
# YOU DON'T NEED TO UNDERSTAND THE CODE BELOW TO SOLVE THE EXCERCISE. 
# JUST IGNORE ANYTHING BELOW THIS LINE AND KEEP SCROLLING DOWN
def derive_key(password, salt=b'mysalt', iterations=10_000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=iterations,
        length=32,  # 32 bytes for AES-256
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))  # url-safe base64-encoded
    return key

def encrypt_text(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    """Returns None if the key is wrong. and the decrypted text otherwise."""
    cipher_suite = Fernet(key)
    try: 
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    except cryptography.fernet.InvalidToken:
        return None
    
    return decrypted_text

# WELCOME BACK, START READING AFTER THIS LINE
# YOU ALSO DON'T NEED TO UNDESRSTAND THE FUNCTION decrypt_text above. 
# but you do need to know that it returns None if the key is wrong and the decrypted text otherwise.
####################################################################################################

encrypted_text = b'gAAAAABlrEOme04y7wp-mtUAtKKS7nT4yE_2jfMtk2HF023BPLOYDNLwhqRCZmaGlB_01kfdinOXZ6uByK_ZDdIzN_QLmIBVBSBWmKZoHevV7YDUwFrNq0eFdH9lfxjXzQr5pP2HA9aLBEek0GRHq6dr0nRKQ-cVKgICOTn70-yiX4fsdzEymO3-FvNMFuMEJZuzL4ORPmvqJs7w2HYSIsrqbghuJcBVikzLkHxkyeZ3S2TLlvsaVbp5LQC-MBKLEWfpP7o6itWRYDQjrwwvC3DkzSdXXCuTmCvDsMlT4rD5hy0w7WZYyJWwx328kgU6QLNuHEZoOcP4'

print("Welcome to the password cracker challenge!")
print("Enter the password to decrypt the text:")
password = input()
key = derive_key(password)
decrypted_text = decrypt_text(encrypted_text, key)
if decrypted_text is None:
    print("Sorry - Wrong password!")
else:
    print(f"{decrypted_text}")
