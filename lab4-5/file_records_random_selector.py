import random

class FileRecordsRandomSelector:
	def __init__(self, file_name):
		self.records = []
		f = open(file_name, 'r');
		for record in f:
			self.records.append(record)
	def get_random_record(self):
		return self.records[random.randint(0, len(self.records) - 1)]
