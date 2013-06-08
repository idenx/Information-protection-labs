from transformers import *
import operator

class AesKey:
	def __init__(self, key, aes_rounds_num, subkey_size):
		WORD_SIZE = 4
		words_in_key = len(key) // WORD_SIZE
		words = [map(ord, key[i * WORD_SIZE : i * WORD_SIZE + WORD_SIZE]) for i in range(words_in_key)]

		global aes_sbox, words_permutator, rcon_sbox
		sub_word = lambda word: aes_sbox.apply(word)
		rotate_word = lambda word: words_permutator.apply(word)
		rcon = lambda x: [rcon_sbox.apply([x])[0], 0, 0, 0]
		xor = lambda a, b: map(operator.xor, a, b)

		subkey_words = subkey_size // WORD_SIZE
		for i in range(words_in_key, (aes_rounds_num + 1) * subkey_words):
			xored_value = words[i - 1]
			if i % words_in_key == 0:
				xored_value = xor(sub_word(rotate_word(xored_value)), rcon(i // words_in_key))
			words.append(xor(words[i - words_in_key], xored_value))
		flatten_list = lambda list_of_lists: [item for sublist in list_of_lists for item in sublist]
		self._subkeys = [flatten_list(words[i * subkey_words : i * subkey_words + subkey_words]) for i in range(len(words) // subkey_words)]

	def subkey(self, index):
		return self._subkeys[index]
