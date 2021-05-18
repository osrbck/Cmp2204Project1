from socket import *
import json
import os
import math
'''''
serverName = 'localhost'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()
'''''

def Chunk_Downloader():
    content_list = [] # To hold the readed available chunk information.
    system_name = []  # To hold the names of chunks of the user requested files.
    recieved_chunks = [] # To hold the chunks that have been downloaded.
    requested_content_dictionary = {} # This is the message system will send to the server, after converting it to json.
    content_name = input(f"Please enter the name of the file you would like to download.")
    full_name = content_name + ".png" # Adding  '.png' to the content name.
    print("Please wait while we verify the file.")
    requested_chunk = 0
    while requested_chunk < 5:
        system_name.append(full_name +"_" + str(requested_chunk+1))  # Making the user entered content name to the same format of the text file.
        requested_chunk = requested_chunk+1
    print(system_name)

    with open('file.txt', 'r') as content_text_file: # Reading local file into a list.
      content_list = json.loads(content_text_file.read())
    content_dictionary = dict(content_list)

    print(f"Content dictionary = {content_dictionary}")  # Converging the list to a dictionary.


    for requested_chunk in system_name:           # Checking and informing the user about availability of the requested chunk.
        if requested_chunk in content_dictionary:

            print(f"{requested_chunk} is available to download on {content_dictionary[requested_chunk]}")    # Informing the user.

            ip_holder = []
            for a in content_dictionary[requested_chunk]:  # Taking the ip's of the available hosts to the list ip_holder.
                ip_holder.append(a)
                print(f"{a} have been added to the ip_holder list")
            print(f"User ip's that can host the {full_name} is/are {ip_holder}")

            key = 'requested_content'
            for c in content_dictionary.keys():                     # Taking the requested chunks into a dictionary.
                requested_content_dictionary.setdefault(key , [])
                requested_content_dictionary[key].append(c)


            requested_content_json = json.dumps(requested_content_dictionary) # Transforming the information in to the json format as stated in 2.3.0-C.
            print(f"Requested contents are {requested_content_json}")         # System will send requested_content_json to the server.


            #Opening up a TCP connection to the desired Ip address.
            # After this part we cant test it before creating Chunk_Uploader.
            # There will be a checking mechanism here to check if the host available, if not it will try the other hosts ftom the ip_holder.
            # Ben burda tek tek chunk isimlerini gönderip indirmeyi planlıyordum. Ama hoca tek seferde tüm requested_content_json ı göndermemizi istiyor.
            # O yüzden burası biraz baştan yapım istiyor.


            serverName = f'{ip_holder[0]}'
            serverPort = 8000
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))


            index = 0
            while index < 5:    # Starting to download the chunks of the file.

                user_request = requested_chunk              # Sending the requested_chunk information to the server. This should be changed to a json with the key requested_content.
                clientSocket.send(requested_chunk.encode())
                downloaded_chunk = clientSocket.recv(1024)    # Recieving the chunk.
                recieved_chunks.append(recieved_chunk)      # Adding the name of the recieved chunk to the recieved_chunks list.
                print(f"{recieved_chunk} have been successfully downlaoded.")   # Informing the user about the successfull download.

                if index == 4:          # Closes the TCP connection when all the chunks are downloaded.
                    clientSocket.close()


                index = index+1


        else:
            print(f"Sorry, your file doesnt seems to exist.")


Chunk_Downloader()