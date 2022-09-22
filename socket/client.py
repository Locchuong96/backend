import cv2 # require installation
import struct # build in function
import pickle # build in function
import socket # build in function

if __name__ == "__main__":

	# create socket
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host_ip = input("Enter server's ip address: ")
	port = input ("Enter server's port number: ")
	client_socket.connect((host_ip,int(port))) # a tuple of string
	message = b""
	payload_size = struct.calcsize("Q")
	while True:
		while len(message) < payload_size:
			packet = client_socket.recv(4*1024) # 4K
			if not packet: break
			message+=packet
		packed_msg_size = message[:payload_size]
		message = message[payload_size:]
		msg_size = struct.unpack("Q",packed_msg_size)[0]
		
		while len(message) < msg_size:
			message += client_socket.recv(4*1024)
		frame_data = message[:msg_size]
		message  = message[msg_size:]
		frame = pickle.loads(frame_data)
		cv2.imshow("RECEIVING VIDEO",frame)
		key = cv2.waitKey(1) & 0xFF
		if key  == ord('q'):
			break
	client_socket.close()