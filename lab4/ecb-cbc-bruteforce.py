import time

from Crypto.Cipher import AES, DES
import base64
import binascii
from Crypto.Random import get_random_bytes

key = bytearray(16)

b64text = "pB5eoahRc0SIJ/L7p9bfIyujdjfvAzjQsOz/sfHtT/jot39uXmvvO5TYDu0nfC2clJNIpYYmGLZGIiXCo3uKoQ=="
b64decoded = base64.b64decode(b64text)


def crypt_ecb():
    for x in range(0, 256):
        for y in range(0, 256):
            key[0] = x
            key[1] = y

            keyenc_aes = binascii.hexlify(key)

            encryptor_aes = AES.new(keyenc_aes.upper(), AES.MODE_ECB)
            cipher_text_aes = encryptor_aes.decrypt(b64decoded)

            try:
                text_decoded = cipher_text_aes.decode()
            except UnicodeDecodeError:
                pass
            else:
                print("Message found: ", text_decoded)
                print("Key found: ", keyenc_aes)


def crypt_cbc():
    for x in range(0, 256):
        for y in range(0, 256):
            key[0] = x
            key[1] = y

            key_enc = binascii.hexlify(key)
            iv = get_random_bytes(16)
            encryptor = AES.new(key_enc.upper(), AES.MODE_CBC, iv)
            cipher_text = encryptor.decrypt(b64decoded)

            try:
                text_decoded = cipher_text.decode()
            except UnicodeDecodeError:
                pass
            else:
                print("Message found: ", text_decoded)
                print("Key found: ", key_enc)


if __name__ == '__main__':
    start_time_cbc = time.time()
    crypt_cbc()
    elapsed_time_cbc = time.time() - start_time_cbc

    start_time_ecb = time.time()
    crypt_ecb()
    elapsed_time_ecb = time.time() - start_time_ecb

    print('des: ' + str(elapsed_time_cbc) + ', ecb: ' + str(elapsed_time_ecb))
