# brutforce na 2 rozne alg ochrony hasel crypt/per/sec
import crypt
import random
from itertools import product
from typing import Iterable

from Crypto.Cipher import ARC4


def codes_to_str(codes: Iterable[int]) -> str:
    return ''.join((chr(c) for c in codes))


def entropy(data: bytes) -> float:
    count = [0] * 256
    data_size = len(data)
    for b in data: count[b] = count[b] + 1

    entropy = 0
    for b in range(256):
        entropy += (count[b] / data_size) * count[b]

    return 1 - entropy / data_size


def brute_force_arc4(cryptogram: bytes, key_length: int = 3, key_alphabet=range(256)) -> None:
    entropy_threshold = 0.9585

    possible_keys = product(key_alphabet, repeat=key_length)
    for k in possible_keys:
        k = codes_to_str(k)
        cipher = ARC4.new(k)
        recovered = cipher.decrypt(cryptogram)
        e = entropy(recovered)

        if e < entropy_threshold:
            return k

    return None

def time1():
    crypt.crypt(''.join(random.choices.))




if __name__ == '__main__':
    haslo = '1234567890'
    hash_haslo = crypt.crypt(haslo, salt='s323efewd4')
    print(hash_haslo)
