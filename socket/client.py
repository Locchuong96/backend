import socket

HEADER = 64 # the number of byte to tell the server wait until it get enough
FORMAT = "utf-8" # format for coding byte
PORT = 5050 # port number
DISCONNECT_MESSAGE = "!DISCONNECT" # content of the disconnect message, if server is received this connection, it will close the connect of that client socket and clean up everything

def send(msg):
	message = msg.encode(FORMAT) # encode the message
	msg_length = len(message) # calculate the byte length in file format
	send_length = str(msg_length).encode(FORMAT) # first send the length of the message
	send_length += b' ' * (HEADER-len(send_length)) # fill the empty space for enough 64 bytes
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

if __name__ == "__main__":
	SERVER_IP = input("What is your server IP address: ")
	if SERVER_IP == "": SERVER_IP = "192.168.1.137"
	ADDR = (SERVER_IP,PORT)
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(ADDR)
	send("Hello Server!") # send the first message
	while True:
		msg = input("Enter Message: ")
		if msg == "exit":
			send(DISCONNECT_MESSAGE)
			break
		else:
			send(msg)
	exit()



