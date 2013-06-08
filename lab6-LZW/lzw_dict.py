import string

_printable_set = set(string.printable)

def _escape_data(data):
	is_printable = lambda str_ : all(c in _printable_set and ord(c) >= 0x20 for c in str_)
	return data if is_printable(data) else '\\' + '\\'.join(map(str, map(ord, data)))

class LzwDict:
	def __init__(self):
		self._words_dict = {chr(i) : i for i in range(256)}
		self._inv_dict = {value : key for key, value in self._words_dict.iteritems()}
		self._max_code = 255
	def add(self, data):
		self._words_dict[data] = self._max_code + 1
		self._inv_dict[self._max_code + 1] = data
		self._max_code += 1
		return self._max_code - 1
	def key(self, value):
		try:
			return self._inv_dict[value]
		except KeyError:
			return None
	def __getitem__(self, data):
		return self._words_dict[data]
	def __contains__(self, item):
		try:
			self._words_dict[item]
		except KeyError:
			return False
		return True
	def __len__(self):
		return len(self._words_dict)
	def __str__(self):
		result = "LzwDict(" + str(len(self._words_dict)) + ") { [0..255] = chr(0)..chr(255), "
		new_keys = [(key, value) for key, value in sorted(self._inv_dict.iteritems()) if key > 255]
		for key, value in new_keys:
			result += str(key) + " : '" + _escape_data(value) + "', "
		return result[:-2] + "}"

