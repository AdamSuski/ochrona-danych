import hashlib
#KDF1


def create_key_simple(secret : bytes, desired_length : int, iterations : int, salt : bytes = b'') -> bytes:
    if desired_length > hashlib.sha256().block_size:
        raise ValueError(f'This function can create keys of max {hashlib.sha256().block_size} size. Recived {desired_length} lenght')

    result = secret
    for i in range(iterations):
        h = hashlib.sha256()
        h.update(result)
        h.update(salt)
        result = h.digest()

    return result[:desired_length]


if __name__ == "__main__":
    key = create_key_simple(b'aa', 8, 1000, b'02')
    key = key.decode("utf-8")
    print("key: " + key)
