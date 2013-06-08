import rsa

PRIVATE_KEY_FILENAME = 'private.key'
PUBLIC_KEY_FILENAME = 'public.key'

def rsa_gen():
	rsa_generator = rsa.Rsa()
	keys = rsa_generator.generate_keys()

	private_file = open(PRIVATE_KEY_FILENAME, 'w')
	private_file.write(keys['private'].to_binary())
	private_file.close()

	public_file = open(PUBLIC_KEY_FILENAME, 'w')
	public_file.write(keys['public'].to_binary())
	public_file.close()

	print('Succesfully generated')

rsa_gen()
