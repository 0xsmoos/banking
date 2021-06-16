def write_file(filename, msg):
	with open(filename, "w") as file:
		file.write(msg)

def read_file(filename):
	with open(filename, "r") as file:
		msg = file.read().split("\n")
	return msg
