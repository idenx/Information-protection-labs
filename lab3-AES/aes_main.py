from aes import Aes
import sys
import os

def main():
	if len(sys.argv) != 3:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' encipher/decipher key"' + os.linesep)
		return 1
	key = sys.argv[2]
	cmd = sys.argv[1]
	input_data = sys.stdin.read()
	cipher_func = Aes.encipher if cmd == 'encipher' else Aes.decipher
	enciphered_data = cipher_func(input_data, key)
	sys.stdout.write(enciphered_data)
	return 0

main()

