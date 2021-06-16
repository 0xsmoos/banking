import socket


port = 24004
host = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f"Socket bound to: {host} | {port}.")
s.listen()
client, client_address = s.accept()

running = True
while running:
	print(f"Connected to: {client_address}.")
	msg = client.recv(1024).decode("utf8")
	if msg != "":
		print(msg)


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

demitri = Account("demitri")
# demitri.add

