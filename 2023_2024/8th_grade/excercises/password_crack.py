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

def encrypt_text(text, password):
    cipher_suite = Fernet(derive_key(password))
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, password):
    """Returns None if the key is wrong. and the decrypted text otherwise."""
    cipher_suite = Fernet(derive_key(password))
    try: 
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    except cryptography.fernet.InvalidToken:
        return None
    
    return decrypted_text

# WELCOME BACK, START READING AFTER THIS LINE
# YOU ALSO DON'T NEED TO UNDESRSTAND THE FUNCTION decrypt_text above. 
# but you do need to know that it returns None if the key is wrong and the decrypted text otherwise.
####################################################################################################

encrypted_text = b'gAAAAABmSvKvFIK4LTeEXR5-Q5MZ7UUCYrjcIH9YJ9D_50MTdfoQ1OyMa2FsXaiKFo0SAWrV5tXvQ79iZUhZlIR5obbCibRo-LYDl7qxwv96MAyy0rdU3hwfzKo02sRlGR-U3YApiOp3t3geMrG2uw9sKwVE_nFy_q2MJzeC9ulariADiZCDS9Uguw62Op1bVgPB_f15Y-SwqSpaaLxElj-UCP4Vb4aaiJ5esim1ojRGs20PfYQUXTbTDnzNl2YCeYijA8_On61uy7Y2tsO0p196uhfRg2Z5eMlqf9rUfBQdquliwPCZK3QeEOn6qjVhw4R2zB8I41YtSYQiERWrVSkxmsIHyAsTEo67cHshfIIh4sPajtixyIYRrqoRHhpb8TU732KbPGR_et4wsxmgcwX2F6d3nemKkms1Hsym4E477-0ZDHvzoY9aqFG3Z9sccucvu2iyzt6GFL5n4N6PJCam1iwou8Ra_iTegYz3nMzNR6JwWJ_Yusip1Ks9Tdh2kwA_lBM9BOiViTcF_WkrNKQPGeYB2TUvsQ=='

print("Welcome to the password cracker challenge!")
print("Enter the password to decrypt the text:")
password = input()

decrypted_text = decrypt_text(encrypted_text, password)
if decrypted_text is None:
    print("Sorry - Wrong password!")
else:
    print(f"{decrypted_text}")
