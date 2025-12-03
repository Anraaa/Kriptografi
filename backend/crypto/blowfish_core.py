from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

BLOCK_SIZE = Blowfish.block_size

def pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    return data[:-pad_len]

def get_cipher(key, iv, mode=Blowfish.MODE_CBC):
    return Blowfish.new(key, mode, iv)
