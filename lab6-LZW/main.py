from __future__ import division
from lzw_compressor import LzwCompressor
import sys
import os

def main():
	if len(sys.argv) != 2:
		sys.stderr.write('Usage: "' + sys.argv[0] + ' compress/decompress"' + os.linesep)
		return 1
	input_data = sys.stdin.read()
	try:
		result = LzwCompressor.compress(input_data) if sys.argv[1] == 'compress' else LzwCompressor.decompress(input_data)
	except Exception:
		sys.stderr.write('Error occured: bad input data format' + os.linesep)
		return 1
	sys.stdout.write(result)
	if sys.argv[1] == 'compress' and input_data:
		sys.stderr.write("Compression coef = " + format(len(result) / len(input_data), '.2f') + os.linesep)
	return 0

main()

