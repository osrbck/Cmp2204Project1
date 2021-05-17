from socket import *
import os
import math
import json

chunk_dict = {"chunks": []}



def Chunk_Anouncer():

    serverIP = 'localhost'
    serverPort = 5001
    server_address = (serverIP, serverPort)

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    print("Client is redy to anounce chunks.")

    host_file_name = input("Please enter the name of the file you would like to host: ")
    host_file_name = host_file_name + ".png"
    host_file_size = os.path.getsize(host_file_name)
    print("Your file is ",host_file_size," kbs")
    CHUNK_SIZE = math.ceil(math.ceil(host_file_size) / 5)
    print("Your file is ", CHUNK_SIZE," chunks.")
    print("Chunks are now starting to be anounced to the local network.")

    key = "chunks"
    index = 1
    with open(host_file_name, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
        while chunk:
            chunkname = host_file_name + '_' + str(index)
            chunk_dict[key].append(chunkname)

            print("chunk name is: " + chunkname + "\n")
            with open(chunkname, 'wb+') as chunk_file:
                chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))

        chunk_json = json.dumps(chunk_dict)
        clientSocket.sendto(chunk_json.encode("utf-8"), server_address)
        print("Your hosting information has been uploaded to the server.")
        modifiedMessage, server = clientSocket.recvfrom(2048)
        print(chunk_json)
        chunk_file.close()



    ''''
    message = input('Input lowercase sentence:')

    clientSocket.sendto(message.encode("utf-8"), server_address)

    modifiedMessage, server = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode("utf-8"))

    clientSocket.close()
    '''''
Chunk_Anouncer()