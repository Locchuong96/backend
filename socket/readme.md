### What is a network Socket

- A software structure within a network node
- Serves as an endpoint to `send` & `receive` data
- Its properties are defined by network API
- Exists ibky during process of application
- Externally identified by its socket address

**Socket addresses**

- A combination of protocol type, IP address and Port number for data communication

- A remote process establishes a socket in its protocol stack

- Remote process then uses networking API to connect to the application

- It Presents its own socket address for use

### Implementation of Sockets

In standard internet protocols like `TCP` and `UDP`: socket address is the combination of:`socket address = (IP address,port number)`

*Much like:
Telephone number and extension*

###  Several types of internet sockets

**Datagram sockets**

- Connectionless sockets `User Datagram Protocol (UDP)`
- Each packet sent or received is individually addressed
- Order and reliability are not guaranteed

**Stream sockets**

- Connection-oriented sockets `Transmission Control Protocol (TCP)`
- Packets are sequenced with a unique flow of error-free data 
- Order and reliability are guaranteed

**Raw sockets**
- Allow direct sending and receiving of IP packets
- Without any protocol-specific transort layer formatting
- When transmitting packets automatic addition of a header is optional
- Mostly used in security-related applications
- Raw sockets are typically available in network equipments

### Python Socket

**Server module**


		[Socket creation] server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			|
			v
	  	  [Socket bind]   server_socket.bind((host_ip,port))
			|
			V
	 	 [Socket listen]  server_socket.listen(5) # 5 is backlog
	 		|
	 		V
	 	[Socket accept]   client_socket,addr = server_socket.accept()
	 		|
	 		V
	 	 [Handle client]  client_socket.recv() or client_socket.send() or client_socket.sendall()
	 		|
	 		V
	  	 [Close client]   client_socket.close()

**Client module**

		[Socket creation] client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			|
			v
	  	  [Socket connect]   client_socket.connect((host_ip,port))
			|
			V
	 	 [Socket receive]  packet = client-socket.recv(1024) # 1024 is buffer size
	 		|
	 		V
	 	[Socket send]   client_socket.send(packet)
	 		|
	 		V
	  	 [Close socket]   client_socket.close()

*Note size of buffer size must be from 64-1064 kB*

### Video data tranmission

At server side

- With OpenCV get video frames of webcam
- With `pickle` serialize frame to byte data
- Pack each frame data using `struct` module
- Send data to client and display frame

At client side

- Receive packets and append them to data
- Unpack the data using `stuct` module
- Load the frame unsing `pickle`
- Display the frame at client side

How to find the IP address

- The IP address is IPv4 Address 

- On `Windows`: `ipconfig/all`

- On `Linux`: `ip addr`

### Workflow 

![workflow](./imgs/serverclienttcp.png)

### References

[Socket programming and OpenCv in Python | webcam video transmit and receive over wifi in Python](https://www.youtube.com/watch?v=7-O7yeO3hNQ&list=PLsM05n4rlXWQCDgMkJ3col-FuhBbBUKgy&index=44) | [Socket programming and OpenCv in Python](https://pyshine.com/Socket-programming-and-openc/)

[Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc&list=PLsM05n4rlXWQCDgMkJ3col-FuhBbBUKgy&index=45)

[Using Python, OpenCV and websockets for camera frames](https://nickhuber.ca/blog/python-opencv-camera-websockets)

[hello-websocket](https://github.com/vmlaker/hello-websocket)