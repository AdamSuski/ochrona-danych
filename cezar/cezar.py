import re


def ceasar(string, key=10):
    string = string.lower()
    string = re.sub(r'[^a-z]', '', string)
    to_return = ''
    for i in string:
        char = ord(i) + key
        if char > ord('z'):
            char -= 26
        to_return += chr(char)
    return to_return


if _name_ == "_main_":
    string = input("Podaj\n")

    encrypted = ceasar(string)

    print(f"zaszyfrowane: {encrypted}")

    decrypted = ceasar(encrypted, key=16)

    print(f"odszyfrowane: {decrypted}")