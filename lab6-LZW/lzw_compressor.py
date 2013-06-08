from lzw_dict import LzwDict
from  bitstring import Bits, BitStream, BitArray
import sys

_LZW_NUM_SIZE = 12

def _lzw_pack_compressed(ints_arr):
	pack_format = 'uint:' + str(_LZW_NUM_SIZE) + '='
	return Bits().join([pack_format + str(num) for num in ints_arr]).tobytes()

def _lzw_unpack_compressed(packed_ints):
	ints_count = len(packed_ints) * 8 // _LZW_NUM_SIZE;
	bits = Bits(bytes=packed_ints, length=ints_count * _LZW_NUM_SIZE)
	return [chunk.uint for chunk in bits.cut(_LZW_NUM_SIZE)]

class LzwCompressor:
	_LZW_MAX_DICT_SIZE = pow(2, _LZW_NUM_SIZE) - 1

	@staticmethod
	def compress(data):
		lzw_dict = LzwDict()
		result = []
		seq = ''
		for c in data:
			next_seq = seq + c
			if next_seq in lzw_dict:
				seq = next_seq
				continue
			lzw_dict.add(next_seq)
			result.append(lzw_dict[seq])
			seq = c
			if len(lzw_dict) == LzwCompressor._LZW_MAX_DICT_SIZE:
				lzw_dict = LzwDict()
		if seq:
			result.append(lzw_dict[seq])

#		print(lzw_dict)
#		print(zip(map(lzw_dict.key, result), result))
		return _lzw_pack_compressed(result)

	@staticmethod
	def decompress(packed_data):
		data = _lzw_unpack_compressed(packed_data)
		if not data:
			return ''
		lzw_dict = LzwDict()
		result = seq = chr(data.pop(0))
		for c in data:
			value = lzw_dict.key(c)
			if value is not None:
				entry = value
			elif c == len(lzw_dict):
				entry = seq + seq[0]
			else:
				raise Exception()

			result += entry
			lzw_dict.add(seq + entry[0])
			if len(lzw_dict) == LzwCompressor._LZW_MAX_DICT_SIZE:
				lzw_dict = LzwDict()
			seq = entry
		return result

