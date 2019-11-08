import ast
import itertools

from Cryptodome.Cipher import AES


def encrypt_CCM(data, key, nonce):
	cipher = AES.new(key, AES.MODE_CCM, nonce)
	ciphertext = cipher.encrypt(data)
	tag = cipher.digest()
	return ciphertext, tag


def decrypt_CCM(ciphertext,key,nonce,tag):
	cipher = AES.new(key, AES.MODE_CCM, nonce)

	plaintext = cipher.decrypt(ciphertext)

	try:
		cipher.verify(tag)
	except ValueError:
		return False

	return plaintext


if __name__ == '__main__':
	with open('dict.txt', 'r') as file:
		text = file.read()
		dictionary = ast.literal_eval(text)
		ciphertext = dictionary['ciphertext']
		tag = dictionary['tag']
		keys = dictionary['keys']
		nonces = dictionary['nonces']
	for iterator in itertools.product(keys, nonces):
		decrypted = decrypt_CCM(ciphertext, iterator[0], iterator[1], tag)
		if decrypted:
			print("Odszyfrowano! Twoja wiadomość:")
			print(decrypted)
			print(f"key: {iterator[0]}, nonce: {iterator[1]}")
		else:
			print("Niepoprawne odszyfrowanie!")
