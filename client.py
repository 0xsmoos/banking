import socket

port = 24004
# host = socket.gethostbyname(socket.gethostname())
host = "ianmc.ga"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Test!")

print("client connected to the network", host)