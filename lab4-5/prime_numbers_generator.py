import rsa_global
import file_records_random_selector

class PrimeNumbersGenerator:
	def __init__(self):
		self.file_records_selector = FileRecordsRandomSelector(rsa_global.PRIME_NUMBERS_FILE)
	def generate(self):
		return int(self.file_records_selector.get_random_record())
