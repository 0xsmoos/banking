import server


client = server.Client(host="ianmc.ga")



def sign_up(name, balance):
	client.create_new_account(name, balance)
	
# account = server.Account("Ian", 100)
# print(account.add(200))


if __name__ == "__main__":
	client.connect()
	client.run()
