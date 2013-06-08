from transformers import *
import operator


class AesState:
	def __init__(self, data):
		self._data = map(ord, data)
	def data(self):
		return map(chr, self._data)

	def sub_bytes(self, inv=False):
		global aes_sbox
		self._data = aes_sbox.apply(self._data) if inv == False else aes_sbox.apply_inv(self._data)
	def shift_rows(self, inv=False):
		global shift_rows_permutator
		self._data = shift_rows_permutator.apply(self._data) if inv == False else shift_rows_permutator.apply_inv(self._data)
	def add_round_key(self, round_key):
		if len(round_key) != len(self._data):
			raise Exception('Lengths of round key and state data are not equal: ' + str(len(round_key)) + ' and ' + str(len(self._data)))
		xor = lambda a, b: map(operator.xor, a, b)
		self._data = xor(self._data, round_key)
	def mix_columns(self, inv=False):
		COL_SIZE = 4 # column size
		gf_mul_vector = (2, 1, 1, 3) if inv == False else (14, 9, 13, 11) # Galois field multiplication vector
		flatten_list = lambda list_of_lists: [item for sublist in list_of_lists for item in sublist]
		self._data = [AesState._mix_column(self._data[i * COL_SIZE : i * COL_SIZE + COL_SIZE], gf_mul_vector) for i in range(len(self._data) // COL_SIZE)]
		self._data = flatten_list(self._data)

# mathematics ---------------------------
	@staticmethod
	def _gf_mult(a, b):
		p = 0
		for _ in range(8):
			if b & 1:
				p ^= a
			a <<= 1
			if a & 0x100:
				a ^= 0x1b
			b >>= 1
		return p & 0xff

	@staticmethod
	def _mix_column(column, mul_vector):
		COL_SIZE = 4 # column size
		res = []
		for i in range(COL_SIZE):
			t = 0
			for j in range(COL_SIZE):
				t ^= AesState._gf_mult(column[(i - j + COL_SIZE) % COL_SIZE], mul_vector[j])
			res.append(t)
		return res
# mathematics end ----------------------

