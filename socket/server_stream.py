import cv2 # require installation
import struct # build in function
import pickle # build in function
import socket # build in function

port = 9999 # 4 digit-number

if __name__ == "__main__":
	# Socket create
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a socket server streaming type
	host_name = socket.gethostname() # get the host name of socket
	host_ip = socket.gethostbyname(host_name + ".local") # socket.gethostbyname(host_name) get the ip address by host name

	socket_address = (host_ip,port)

	# socket bind
	server_socket.bind(socket_address)
	print(f"Server:\nHOST_NAME: {host_name}\nHOST IP: {host_ip}\nADDRESS: {socket_address}")

	# socket listen
	server_socket.listen(5)
	print(f"LISTENING AT:{socket_address}")

	# socket accept
	while True:
		client_socket,addr = server_socket.accept()
		print(f"GOT CONNECTION FROM:{addr}")
		if client_socket:
			cap = cv2.VideoCapture(0) #create a connection into webcam by opencv
			while(cap.isOpened()):
				ret,frame = cap.read()
				data = pickle.dumps(frame) # 921762 bytes
				message = struct.pack("Q",len(data)) + data # 921770 bytes = 8 bytes + data
				print(f"MESSAGE: {len(message)}")
				client_socket.sendall(message)
				cv2.imshow('TRANSMITING VIDEO',frame)
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					client_socket.close()



