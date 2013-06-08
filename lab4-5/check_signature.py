import sys
import rsa_key
import rsa
import md5

def main():
	if len(sys.argv) != 3:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' signature public.key"\n')
		return 1
	key_file = open(sys.argv[2], 'r')
	key = rsa_key.RsaKey(0, 0)
	key.from_binary(key_file.read())
	rsa_encrypter = rsa.Rsa()
	signature_file = open(sys.argv[1], 'r')

	data_hash = md5.new(sys.stdin.read()).digest()
	decrypted_data_hash = rsa_encrypter.decipher_data(signature_file.read(), key)
	print("Input data is valid" if decrypted_data_hash == data_hash else "Input data is invalid")

main()
