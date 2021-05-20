import re

def valid_ip(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
			if re.match(pattern, line):
				print(line)

valid_ip('ip.txt')