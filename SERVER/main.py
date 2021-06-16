import server
import account


def main():
	server_instance = server.Server()
	server_instance.setup()
	server_instance.run()

	client_account = account.Account()


if __name__ == "__main__":
	main()