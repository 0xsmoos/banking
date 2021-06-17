import media

class Account:
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance

	def add(self, amount):
		self.balance += amount if amount > 0 else 0
		return self.balance

	def subtract(self, amount):
		self.balance -= amount if amount > 0 else 0
		return self.balance
		
	def transfer(self, amount, recipient, sender):
		sender.subtract(amount)
		recipient.add(amount)
		media.write_file(filename, msg)
		return self.balance