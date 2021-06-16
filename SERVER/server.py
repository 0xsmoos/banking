import socket
import account


class Server:
	def __init__(self, host=socket.gethostbyname(socket.gethostname()), port=24004):
		self.host = host
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def bind(self):
		self.s.bind((self.host,self.port))
		print(f"Socket bound to: {self.host} | {self.port}.")

	def listen(self):
		self.s.listen()

	def accept(self):
		self.client, self.client_address = self.s.accept()
		return self.client, self.client_address

	def setup(self):
		self.bind()
		self.listen()
		return self.accept()

	def run(self):
		print(f"Connected to: {self.client_address}.")

		running = True
		while running:
			msg = self.client.recv(1024).decode("utf8")
			if msg == "":
				continue
			if "--new_act==" in msg:
				cmd = msg.split("--new_act==")
				client_account = account.Account(cmd[0], cmd[1])
	