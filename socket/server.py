'''
Server handle multi clients
'''
import socket
import threading
import time

HEADER = 64 # the number of byte to tell the server wait until it get enough
FORMAT = "utf-8" # format for coding byte
PORT = 5050 # port number
DISCONNECT_MESSAGE = "!DISCONNECT" # content of the disconnect message, if server is received this connection, it will close the connect of that client socket and clean up everything
HOST_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(HOST_NAME+".local")
ADDR = (SERVER_IP,PORT)
print(f"HOST_NAME: {HOST_NAME}, SERVER_IP: {SERVER_IP},ADDR: {ADDR}")
# create a server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # category of network, the way you transfer data
server.bind(ADDR) # give the address for server socket

def handle_client(client,addr):
	'''
	handle client socket connect to server socket
	Args:
		client: the client
		addr: address of the client
	'''
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True
	while connected:
		# Read the message length
		msg_length = client.recv(HEADER).decode(FORMAT) # this is a blocking line of code, add how many bytes you want to receive from the arguments
		# If you reveive something
		if msg_length :
		# Read until the message long as msg_length
			if msg_length == DISCONNECT_MESSAGE:
				connected = False # break the whule loop
				print(f"[CLIENT-{addr}]: {DISCONNECT_MESSAGE}")
			msg = client.recv(HEADER).decode(FORMAT)
			print(f"[CLIENT-{addr}]: {msg}")
			client.send("Msg received".encode(FORMAT)) # Sever send back message
	client.close()

def start(server):
	'''
	Function for handle new connection to server for lstening the connection and pass them into hanfle_client
	Args:
		server: socket server object
	'''
	server.listen()
	while True:
		client,addr = server.accept() # wait for the connection,
		# create a thread for client connect to server 
		thread = threading.Thread(target=handle_client,args=(client,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONs] {threading.activeCount()-1}") #-1 because start() is already running on a thread

if __name__ == "__main__":
	print("[STARTING] server is starting...")
	start(server)