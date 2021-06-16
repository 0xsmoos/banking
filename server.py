import socket


port = 24004
host = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f"Socket bound to: {host} | {port}.")
s.listen()


running = True
while running:
	client, client_address = s.accept()
	print(f"Connected to: {client_address}.")


class Account:
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance
		
	def add(self, amount):
		self.balance += amount if amount > 0 else 0
	
	def subtract(self, amount):
		self.balance -= amount if amount > 0 else 0

	# TODO
	def transfer(self, amount, recipient):
		pass

Account("demitri", )
