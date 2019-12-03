from random import randint, randrange
from math import pow, gcd, floor


# Text -> Numbers
def text_to_numbers(text: str, block_size: int) -> list:
    text_blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    result = []
    for block in text_blocks:
        encoded_block = []
        for num in block.encode():
            encoded_block.append(num if (100 <= num < 900) else 999 - num)
        block_to_number = int(''.join(str(i) for i in encoded_block))
        result.append(block_to_number)
    return result


# Numbers -> Text
def numbers_to_text(nums: list, chunk_size: int) -> str:
    result_block_int = []
    result = []
    for num in nums:
        block = list(map(lambda n: int(n), string_to_pieces(str(num), 3)))
        result_block_int.extend(block)
    for integer_result in result_block_int:
        result.append(integer_result if (100 <= integer_result < 900) else 999 - integer_result)
    return ''.join(chr(i) for i in result)


def string_to_pieces(string: str, size: int) -> list:
    return [string[i:i + size] for i in range(0, len(string), size)]


# nums = text_to_numbers('ala ma kota a ola ma psa', 4)
# print(numbers_to_text(nums, 4))


# SITO ERASTOTENESA
def eratostenes(n: int):
    multiples = set()
    primes = set()
    for i in range(2, n + 1):
        if i not in multiples:
            primes.add(i)
            for j in range(i * i, n + 1, i):
                multiples.add(j)
    return n in sorted(primes), sorted(primes)


print(eratostenes(13))


# FERMAT
def get_coprime_number(n: int):
    while True:
        coprime = randrange(n)
        if gcd(coprime, n) == 1:
            return coprime


# a^(n-1) % n == 1 to liczba n jest pierwsza
def fermat(n: int, k: int) -> bool:
    for _ in range(k):
        a = get_coprime_number(n)
        if pow(a, n - 1) % n != 1:
            return False
    return True


print(fermat(6, 100))


# Algorytm euklidesa
def eu_nwd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# print(eu_nwd(10, 130))

# Liczby wzglednie pierwsze - sprawdzenie
def rel_prime(a: int, b: int):
    return eu_nwd(a, b) == 1


# print(rel_prime(7, 13))

# Rozszerzony Euklides
def euclidian_gcd_extended(a: int, b: int):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = euclidian_gcd_extended(b % a, a)
        return g, x - (b // a) * y, y


def modinv(number: int, modulo: int) -> int:
    g, x, y = euclidian_gcd_extended(number, modulo)
    if g != 1:
        return None
    else:
        return x % modulo


# print(modinv(21, 43))

# szybkie potegowanie modularne
def powmod(a: int, k: int, n: int) -> int:
    # a ** k % n
    b = bin(k)[2:]
    result = 1
    x = a % n
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '1':
            result = result * x % n
        x **= 2
        x %= n
    return result


# print(powmod(5, 117, 19))

# Napisz pełny program generujący klucze RSA.
def generate_primes():
    primes = eratostenes(100000)[1]
    k = randint(0, len(primes) - 1)
    temp = randint(0, len(primes) - 1)
    l = (k + 1) % len(primes) if temp == k else temp
    return primes[k], primes[l]


def get_rsa():
    p, q = generate_primes()
    n = p * q
    euler = (p - 1) * (q - 1)
    e = 65537
    while not rel_prime(e, euler):
        e = get_coprime_number(euler)
    d = modinv(e, euler)
    return (n, d), (n, e)


print(get_rsa())


# Napisz program realizujący szyfrowanie RSA
def crypt_rsa(text_to_encrypt: int, public_key: tuple, piece_size: int = 2) -> list:
    # enc = (block ** e) % modulo
    text_to_encrypt = str(text_to_encrypt)
    modulo, e = public_key
    numbers = text_to_numbers(text_to_encrypt, piece_size)
    decrypted = []
    for block in numbers:
        decrypted.append(powmod(block, e, modulo))
    return decrypted


def decrypt_rsa(crypted: list, private_key: tuple, piece_size: int = 2) -> str:
    # msg = (block ** d) % modulo
    modulo, d = private_key
    encrypted = []
    for block in crypted:
        encrypted.append(powmod(block, d, modulo))
    return numbers_to_text(encrypted, piece_size)


private_key, public_key = get_rsa()

crypted = crypt_rsa(123467890, public_key)

print(crypted)

print(decrypt_rsa(crypted, private_key))
