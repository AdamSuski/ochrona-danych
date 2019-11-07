from collections import Iterable
from itertools import product
from same_zeros import entropy
from Crypto.Cipher import DES


def codes_to_str(codes : Iterable[int]) -> str:
    return ''.join((chr(c) for c in codes))


def brute_force_des(cryptogram: bytes, key_alphabet=range(256)) -> None:
    entropy_threshold = 0.965

    possible_keys = product(key_alphabet, repeat=8)
    for k in possible_keys:
        k = codes_to_str(k)

        des = DES.new(k, DES.MODE_ECB)
        recovered = des.decrypt(cryptogram)

        e = entropy(recovered)
        if e < entropy_threshold:
            print('\nZnaleziono rozwiązanie!\n')
            print(f'Klucz: {k}')
            print(f'Wiadomość: {recovered}')
            return

    print(f'Nie znaleziono rozwiązania')


if __name__ == "__main__":
    key = 'abcabdbb'
    data = padd_data(poem.encode(), 8)

    des = DES.new(key, DES.MODE_ECB)
    cryptogram = des.encrypt(data)

    keyAlphabet = list(range(ord('a'), ord('e') + 1))
    # bruteforceDES(cryptogram, keyAlphabet)

