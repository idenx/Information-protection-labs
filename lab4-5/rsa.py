import number_generators
import rsa_key
import struct

def calc_eulers_func(p, q): # p and q must be prime
	return (p - 1) * (q - 1)

def gcdex(a, b, params):
	if a == 0:
		params[0] = 0
		params[1] = 1
		return b
	new_params = [0, 0]
	d = gcdex(b % a, a, new_params)
	params[0] = new_params[1] - (b / a) * new_params[0]
	params[1] = new_params[0]
	return d

def demultiplicate(num, modulus):
	params = [0, 0]
	gcdex(num, modulus, params)
	x = params[0]
	x = (x % modulus + modulus) % modulus
	return x

def create_keys():
	prime_numbers_generator = number_generators.PrimeNumbersGenerator()
	prime1 = prime_numbers_generator.generate()
	prime2 = prime1
	while prime2 == prime1:
		prime2 = prime_numbers_generator.generate()
	modulus = prime1 * prime2
	fermat_numbers_generator = number_generators.FermatNumbersGenerator()
	public_exponent = fermat_numbers_generator.generate()
	eulers_func = calc_eulers_func(prime1, prime2)
	private_exponent = demultiplicate(num=public_exponent, modulus=eulers_func)

	return {'private' : rsa_key.RsaKey(private_exponent, modulus), 'public' : rsa_key.RsaKey(public_exponent, modulus)}

class Rsa:
	def generate_keys(self):
		return create_keys()

	def encipher_data(self, data, public_key):
		public_exponent = public_key.num()
		modulus = public_key.modulus()
		nums = [pow(ord(char), public_exponent, modulus) for char in data]
		res = bytearray(len(nums) * 8)
		offset = 0
		for num in nums:
			struct.pack_into('Q', res, offset, num)
			offset += 8
		return res

	def decipher_data(self, data, private_key):
		private_exponent = private_key.num()
		modulus = private_key.modulus()
		nums_count = len(data) / 8
		nums = struct.unpack(str(nums_count) + 'Q', data)
		return ''.join([chr(pow(num, private_exponent, modulus)) for num in nums])

