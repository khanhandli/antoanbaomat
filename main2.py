LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_cipher(message, key, MODE):
	translated = []
	keyIndex = 0
	key = key.upper()

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			if MODE.upper() == 'ENCRYPT':
				num += LETTERS.find(key[keyIndex])
			elif MODE.upper() == 'DECRYPT':
				num -= LETTERS.find(key[keyIndex])
			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num])
			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(symbol)
	return ''.join(translated)


def main():
	message = "we are discovered, save yourself"

	key = 'DECEPTIVE'
	cipher = vigenere_cipher(message, key, 'ENCRYPT')
	print('nMessage:               ' + message)
	print('nCiphertext:            ' + cipher)

	message = vigenere_cipher(cipher, key, 'DECRYPT')
	print('nMessage after decrypt: ' + message)


if __name__ == '__main__':
	main()