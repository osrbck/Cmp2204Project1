from socket import *

'''''
def Open_TCPServer():
	global serverPort
	serverPort = 8000
	global serverSocket
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	print("Server is ready to recieve.")


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
'''''



