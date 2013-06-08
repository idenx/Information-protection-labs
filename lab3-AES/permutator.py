
class Permutator:
	def __init__(self, permutations, reversed_permutations=None):
		self._permutations = permutations
		self._rev_permutations = reversed_permutations
	def apply(self, data):
		return [data[self._permutations[i]] for i in range(len(data))]
	def apply_inv(self, data):
		if self._rev_permutations is not None:
			return [data[self._rev_permutations[i]] for i in range(len(data))]
		return [data[self._permutations.index(i)] for i in range(len(data))]
