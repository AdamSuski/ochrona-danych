# atak na bmp
import itertools

from Crypto.Cipher import AES, DES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from PIL import Image

from same_zeros import entropy


def data_padding(data):
    size = 16 - len(data) % 16
    for i in range(size):
        data += b'a'
    return (data, size)


def decrypt_cbc(data, key):
    key = PBKDF2(bytes(key.encode('utf-8')), b'abc')
    iv = b'0000000000000000'

    cbc = AES.new(key, AES.MODE_CBC, iv)
    data, size = data_padding(data)
    return cbc.decrypt(data)[:-size]


if __name__ == "__main__":
    data = b''
    img_in = Image.open('we800_CBC_encrypted.bmp')
    rgb = img_in
    data = img_in.convert('RGB').tobytes()
    ent = 1
    for i in itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f'], 3):
        decrypted_data = decrypt_cbc(data, ''.join(i))
        if entropy(decrypted_data) < ent:
            ent = entropy(decrypted_data)
            rgb = convert_to_RGB(decrypted_data)
            print(ent, i)

    image = Image.new(img_in.mode, img_in.size)
    image.putdata(rgb)
    image.save('decypted.bmp', 'bmp')