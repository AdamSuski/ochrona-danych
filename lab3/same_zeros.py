# Porównaj ECB i CBC (entropia) dla tekstu jawnego o zerowej entropii
from collections import Counter
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCK_SIZE = 8


def zero_byte_file():
    text = chr(0)
    for i in range(10):
        text += text
    return text


def entropy(b):
    d = Counter(b)
    e = 0
    for keys in d:
        e += d[keys] * d[keys] / len(b)
    return 1 - e / len(b)


if __name__ == "__main__":
    with open('nullbytes', 'rb') as f:
        data = f.read()
    # data = zero_byte_file()
    print(entropy(data))
    # print(data)
    key = '12345678'
    iv = get_random_bytes(8)
    ecb = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_ecb = ecb.encrypt(pad(data, BLOCK_SIZE))
    # print(encrypted_ecb)
    print('ecb')
    print(entropy(encrypted_ecb))
    cbc = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)
    encrypted_cbc = cbc.encrypt(pad(data, BLOCK_SIZE))
    # print(encrypted_cbc)
    print('cbc')
    print(entropy(encrypted_cbc))
