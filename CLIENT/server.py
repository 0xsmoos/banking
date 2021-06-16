import socket


class Client:
	def __init__(self, host="ianmc.ga", port=24004):
		self.host = host
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.s.connect((self.host, self.port))
		# self.s.send(b"Test!")
		print("client connected to the network", self.host)

	def send(self, msg, encoding="utf8"):
		if msg != "":
			msg = msg.encode(encoding)
			self.s.send(msg)

	def recv(self, buffer=1024, encoding="utf8"):
		msg = self.s.recv(buffer).decode(encoding)
		return msg if msg != "" else None

	def create_new_account(self, name, bal=0):
		msg = f"--new_act=={name}|{bal}"
		self.send(msg)

	def run(self):
		running = True
		while running:
			self.s.send(input("Enter a message:\n> ").encode("utf8"))

if __name__ == "__main__":
	client = Client()
	client.send("hello ther!")
