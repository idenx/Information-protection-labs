import sys
import rsa_key

def rsa_key_cat():
	if len(sys.argv) != 2:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' some.key"\n')
		return 1
	f = open(sys.argv[1], 'r')
	key = rsa_key.RsaKey(0, 0)
	key.from_binary(f.read())
	print(key.to_string())
	return 0

rsa_key_cat()

