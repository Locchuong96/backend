import cv2 # require installation
import struct # build in function
import pickle # build in function
import socket # build in function

if __name__ == "__main__":

	# create socket
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host_ip = input("Enter server's ip address: ")
	if host_ip == "": host_ip = '192.168.1.137' # if you press enter, set default value
	port = input ("Enter server's port number: ")
	if port == "": port = '9999' # if you press enter, set default value
	client_socket.connect((host_ip,int(port))) # a tuple of string
	message = b""
	print(f"message's size: {len(message)}")
	payload_size = struct.calcsize("Q") # calculate size of "Q" character 8 bytes [frame_size+frame]
	print(f"payload_size: {payload_size} \n")
	while True:
		# Starting to read a full-package message = b"" right here
		while len(message) < payload_size: # Read buffer until the message bigger than 8 bytes (Q char size)
			packet = client_socket.recv(4*1024) # 4KB buffer size
			if not packet: break
			message += packet # 1 can be turn to 0 but 0 is never turn to 0, keep add until the message is complete
			print(f"Receiving packets message's size {len(message)}") 
		print(f"Out payload message's size: {len(message)}")

		packed_msg_size = message[:payload_size] # 921762 + frame
		message = message[payload_size:]
		msg_size = struct.unpack("Q",packed_msg_size)[0] # int
		print(f"packed_msg_size: {len(packed_msg_size)}, message: {len(message)}, msg_size: {msg_size}\n")
		
		# continuosly read until message enough a frame
		while len(message) < msg_size:
			message += client_socket.recv(4*1024)
			#print(f"Reading a frame, message: {len(message)}")
		
		frame_data = message[:msg_size]
		message = b"" # message  = message[msg_size:], reset message message = 0 bytes
		frame = pickle.loads(frame_data)
		
		cv2.imshow("RECEIVING VIDEO",frame)
		key = cv2.waitKey(1) & 0xFF
		if key  == ord('q'):
			break
	client_socket.close()