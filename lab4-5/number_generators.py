from file_records_random_selector import *

FERMAT_NUMBERS_FILENAME = 'fermat.numbers'
PRIME_NUMBERS_FILENAME = 'prime.numbers'

class FermatNumbersGenerator:
	def __init__(self):
		self.__records_selector = FileRecordsRandomSelector(FERMAT_NUMBERS_FILENAME)
	def generate(self):
		return int(self.__records_selector.get_random_record())

class PrimeNumbersGenerator:
	def __init__(self):
		self.__records_selector = FileRecordsRandomSelector(PRIME_NUMBERS_FILENAME)
	def generate(self):
		return int(self.__records_selector.get_random_record())
