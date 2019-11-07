import re


def repeat_until_length(txt, length):
    x = int(length / len(txt)) + 1
    return (txt * x)[:length]


def vigenere(string, key):
    string = string.lower()
    key = key.lower()
    string = re.sub(r'[^a-z]', '', string)

    key = repeat_until_length(key, len(string) + 1)
    to_return = ''
    for i in range(0, len(string)):
        char = ord(string[i]) + ord(key[i]) - 2 * ord('a')
        char = char % 26 + ord('a')
        to_return += chr(char)
    return to_return


def main(args):
     string = input("Podaj napis\n")
     key = input("Podaj klucz\n")

     encrypted = vigenere(string, key)

     print(f"zaszyfrowane: {encrypted}")


if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))
