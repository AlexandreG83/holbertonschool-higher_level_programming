#!/usr/bin/python3
"""Print the ASCII lowercase alphabet without q and e in one line"""
for i in range(97, 123):
	if chr(i) != 'e' and chr(i) != 'q':
		print("{}".format(chr(i)), end="")
