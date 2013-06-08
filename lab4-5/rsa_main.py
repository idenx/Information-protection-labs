import rsa
import rsa_key
import sys




def rsa_main():
	if len(sys.argv) != 3:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' encipher/decipher public/key/private.key"\n')
		return 1
	key_file = open(sys.argv[2], 'r')
	key = rsa_key.RsaKey(0, 0)
	key.from_binary(key_file.read())

	data = sys.stdin.read()
	key_file.close()
	rsa_obj = rsa.Rsa()

	func = rsa_obj.encipher_data if sys.argv[1] == 'encipher' else rsa_obj.decipher_data
	sys.stdout.write(func(data, key))
	return 0

rsa_main()
