import struct

class RsaKey:
	def __init__(self, num, modulus):
		self.__num = num
		self.__modulus = modulus
	def num(self):
		return self.__num
	def modulus(self):
		return self.__modulus
	def to_string(self):
		return 'num = ' + str(self.__num) + ', modulus = ' + str(self.__modulus)
	def to_binary(self):
		return struct.pack('IQ', self.__num, self.__modulus)
	def from_binary(self, binary_data):
		[self.__num, self.__modulus] = struct.unpack('IQ', binary_data)
