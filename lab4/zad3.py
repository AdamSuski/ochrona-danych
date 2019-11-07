# # 2 pliki HTML.  pierwsze 32 bity sei licza
# def trivial_hash(dane):
#     hash = 0
#     for znak in dane:
#         hash += ord(znak)
#     return hash % 999
#
#
# def display_trivial_hash_for_file(file_name : str) -> None:
#     with open(file_name) as file:
#         print(trivial_hash(file.read()))
#
#
# if __name__ == '__main__':
#     display_trivial_hash_for_file('TryvialDocument.html')
#     display_trivial_hash_for_file('FakeTryvialDocument.html')

# Python program to find SHA256 hash string of a file
import hashlib

if __name__ == '__main__':
    filename1 = 'html1.html'
    filename2 = 'html1.html'
    sha256_hash = hashlib.sha256()

    with open(filename1, "rb") as f:
        # Read and update hash string value in blocks of 4K
        byte_block = f.read()
        sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())

    with open(filename2, "rb") as f:
        # Read and update hash string value in blocks of 4K
        byte_block = f.read()
        sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())
