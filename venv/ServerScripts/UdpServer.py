from socket import *
import json

content_dictionary = {}

def Content_Discovery():
	serverPort = 5001

	# Create a UDP socket
	serverSocket = socket(AF_INET, SOCK_DGRAM)

	# Bind the socket to the port
	serverSocket.bind(('', serverPort))
	print("The server is listening the local broadcasts.")

	while True:
		message, clientAddress = serverSocket.recvfrom(2048)
		print('Received {} bytes from {}'.format(len(message), clientAddress))
		print(message) # Printing the incoming message as json
		message_dict = json.loads(message.decode('utf-8')) # Changing the json value to a dictionary
		print(message_dict)
		variable = []
		for i in message_dict['chunks']:  # Taking the items of the key 'chunks' to a list
			variable.append(i)
			print(f"List of variables grow stronger. I have added {i} to our ranks") #

		print(variable)

		for i in variable:    # Trying to make dictionary where the keys are the values of the list variables.
			if i in content_dictionary.keys():  # If the chunk already exists, assigns the ip address of the client to it as an item.
				content_dictionary[i].append(clientAddress[0])
				print(f"I have added {clientAddress} to the existing {i} key in content_dictionary.")
			else:                                          # If the key do not exists creates it, than assigns the ip.
				content_dictionary.setdefault(i, [])
				content_dictionary[i].append(clientAddress[0])
				print(f"I have created the key {i} and added {clientAddress} to as its item. ")

		print(content_dictionary)
		with open('file.txt', 'w') as file:
			file.write(json.dumps(content_dictionary))
		print("Host info has been saved to a text file.")
		#modifiedMessage = message.upper()
		#serverSocket.sendto(modifiedMessage, clientAddress)

#Content_Discovery()     # Chunk_Anouncer ile Chunk_Discovery yi denemek için önce buradaki yorumu kaldırıp UdpServer ı çalıştır.
						 #  Sonra tekrak yoruma alıp main i çalıştır.
						 # Please enter the name of the file you would like to host: çıktığı zaman hey yaz.
