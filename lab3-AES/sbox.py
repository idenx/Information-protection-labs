
class Sbox:
	def __init__(self, mappings, reversed_mappings=None):
		self._mappings = mappings
		self._rev_mappings = reversed_mappings
	def apply(self, data):
		return [self._mappings[byte] for byte in data]
	def apply_inv(self, data):
		if self._rev_mappings is not None:
			return [self._rev_mappings[byte] for byte in data]
		return [self._mappings.index(byte) for byte in data]

