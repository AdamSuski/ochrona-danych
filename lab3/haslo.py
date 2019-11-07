from math import log2

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


def create_key_PBKDF2(password: str):
    salt = get_random_bytes(8)
    return PBKDF2(password=password, salt=salt)


def padding(data: bytes, block_size: int) -> bytes:
    padding = ord('@')
    diff = block_size - len(data) % block_size
    return data + bytes([padding] * diff)


def crypt_file_aes_cbc(filename, key, iv):
    file_bytes = read_bytes_from_file(filename)
    aesCBC = AES.new(key, AES.MODE_CBC, iv)
    encryptedCBC = aesCBC.encrypt(padding(file_bytes, len(key)))
    return encryptedCBC


if __name__ == "__main__":
    with open('haslo.txt', 'r') as file:
        haslo = file.read()
        haslo_bytes = [ord(i) for i in haslo]
        haslo_entropy = count_entropy(haslo_bytes)
        print(haslo_entropy)

    if haslo_entropy < 30:
         print('haslo za slabe')
         haslo = create_key_PBKDF2(haslo)
         print(len(haslo) * log2(256))

    else:
         haslo = bytes([ord(i) for i in haslo])
         iv = get_random_bytes(16)
         encrypted = crypt_file_aes_cbc('new.txt', haslo, iv)
         write_bytes_to_file('new1.txt', encrypted)
