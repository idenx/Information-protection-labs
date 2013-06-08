from aes_key import AesKey
from aes_state import AesState

class Aes:
	_ROUNDS_COUNT = 10
	_STATE_SIZE = 16
	_AES_KEY_LEN = 16
	_BLOCK_SIZE = 16
	_PADDING_VALUE = '\0'

	@staticmethod
	def _do_foreach_block(data, key, ciphering_callback):
		if len(key) != Aes._AES_KEY_LEN:
			raise Exception('Unsupported key length')

		aes_key = AesKey(key, Aes._ROUNDS_COUNT, Aes._STATE_SIZE)
		new_data = [byte for byte in data]
		padding = len(data) % Aes._BLOCK_SIZE if len(data) != 0 else Aes._BLOCK_SIZE
		for _ in range(padding):
			new_data.append(Aes._PADDING_VALUE)
		blocks_count = len(new_data) // Aes._BLOCK_SIZE
		blocks = [new_data[i * Aes._BLOCK_SIZE : i * Aes._BLOCK_SIZE + Aes._BLOCK_SIZE] for i in range(blocks_count)]

		process_list = lambda list_of_lists: ''.join([item for sublist in list_of_lists for item in sublist])
		return process_list([ciphering_callback(block, aes_key) for block in blocks])

	@staticmethod
	def _encipher_block(data, aes_key):
		if len(data) != Aes._BLOCK_SIZE:
			raise Exception('Invalid block size')
		state = AesState(data)

		state.add_round_key(aes_key.subkey(0))
		for i in range(1, Aes._ROUNDS_COUNT - 1):
			state.sub_bytes()
			state.shift_rows()
			state.mix_columns()
			state.add_round_key(aes_key.subkey(i))
		state.sub_bytes()
		state.shift_rows()
		state.add_round_key(aes_key.subkey(Aes._ROUNDS_COUNT - 1))

		return state.data()

	@staticmethod
	def _decipher_block(data, aes_key):
		if len(data) != Aes._BLOCK_SIZE:
			raise Exception('Invalid block size')
		state = AesState(data)

		state.add_round_key(aes_key.subkey(Aes._ROUNDS_COUNT - 1))
		for i in reversed(range(1, Aes._ROUNDS_COUNT - 1)):
			state.shift_rows(inv=True)
			state.sub_bytes(inv=True)
			state.add_round_key(aes_key.subkey(i))
			state.mix_columns(inv=True)
		state.shift_rows(inv=True)
		state.sub_bytes(inv=True)
		state.add_round_key(aes_key.subkey(0))

		return state.data()

	@staticmethod
	def encipher(data, key):
		return Aes._do_foreach_block(data, key, Aes._encipher_block)

	@staticmethod
	def decipher(data, key):
		return Aes._do_foreach_block(data, key, Aes._decipher_block)


