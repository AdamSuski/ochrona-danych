import re


def ceasar(napis, klucz=10):
    napis = napis.lower()
    napis = re.sub(r'[^a-z]', '', napis)
    to_return = ''
    for i in napis:
        char = ord(i) + klucz
        if char > ord('z'):
            char -= 26
        to_return += chr(char)
    return to_return


def main(args):
    string = input("Podaj napis\n")

    zaszyfrowane = ceasar(string)

    print(f"zaszyfrowane: {zaszyfrowane}")

    odszyfrowane = ceasar(zaszyfrowane, 16)

    print(f"odszyfrowane: {odszyfrowane}")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
