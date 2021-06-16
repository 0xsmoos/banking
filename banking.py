import datetime
import hashlib
import json
addresses = ["j", "will"]


class Chain:
	def __init__(self, name, balance, address):
		global addresses
		self.name    = name
		self.balance = balance
		self.address = address
		self.chain   = []
        #self.create_block(previous_hash = '0')
		addresses.append(self.address)


	def create_block(self):
	        block = {'index': len(self.chain) + 1,
	                 'timestamp': str(datetime.datetime.now())}
	        self.chain.append(block)
	        return block

	def hash(self, block):
	        encoded_block = json.dumps(block, sort_keys = True).encode()
	        return hashlib.sha256(encoded_block).hexdigest()

	# def menu(self):
	# 	selection = input("Welcome to sieNet. What would you like to do?")
	# 	if selection == "Send money":
	# 		send_money()
	# 	if selection == "Menu":
	# 		menu()
	# 	if selection == "Print the last block":
	# 		get_previous_block()
	# def sign_in(self):
	# 	menu()
# 	def start_program(self):
# 		option1 = input("Welcome to SIE banking and trading. Please Sign in or create an account:\n'Create account'\n'Sign in' ")
# 		if option1 == "Create account":
# 			create_person()
# 		if option1 == "Sign in":
# 			sign_in()

	# def send_money(self):
	# 	amount = input(str("how much money would you like to send?"))
	# 	recipient_addy = input(str("where would you like to send the money to?"))
	# 	if recipient_addy not in addresses:
	# 		print("invalid address")
	# def create_person(self):
	# 	name = input("input name\n")
	# 	balance = "0"
	# 	address = "1234"
	# 	Chain(name, balance, address)