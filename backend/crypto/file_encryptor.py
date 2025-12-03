from .blowfish_core import *
from .kdf import derive_key

CHUNK = 4096

def encrypt_file(input_path, output_path, password):
    key = derive_key(password)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = get_cipher(key, iv)

    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(iv)
        while chunk := f_in.read(CHUNK):
            padded = pad(chunk)
            encrypted = cipher.encrypt(padded)
            f_out.write(encrypted)


def decrypt_file(input_path, output_path, password):
    with open(input_path, "rb") as f_in:
        iv = f_in.read(BLOCK_SIZE)

        key = derive_key(password)
        cipher = get_cipher(key, iv)

        with open(output_path, "wb") as f_out:
            while chunk := f_in.read(CHUNK):
                decrypted = cipher.decrypt(chunk)
                unpadded = unpad(decrypted)
                f_out.write(unpadded)
