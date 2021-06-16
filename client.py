import socket

port = 24004
# host = socket.gethostbyname(socket.gethostname())
host = "ianmc.ga"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b"Test!")

print("client connected to the network", host)

running = True
while running:
	s.send(input("Enter a message:\n> ").encode("utf8"))