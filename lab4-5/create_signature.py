import sys
import rsa_key
import rsa
import md5

def main():
	if len(sys.argv) != 2:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' private.key"\n')
		return 1
	f = open(sys.argv[1], 'r')
	key = rsa_key.RsaKey(0, 0)
	key.from_binary(f.read())
	rsa_encrypter = rsa.Rsa()

	sys.stdout.write(rsa_encrypter.encipher_data(md5.new(sys.stdin.read()).digest(), key))

main()
