import math
import os
from ServerScripts import UdpServer, UdpClient, TcpServer
content_name = ""
filename = ""


# Son versiyonda UdpServer olmayacak içindeki kod Client a atılacak şuanlık yalnızca test için böyle.
# Nasıl test edileceği UdpServer ın son kısmında yazıyor.

# asdf

'''
def get_file_name():
    content_name = input("Please enter the name of the file you would like to download.")
    filename = content_name + ".png"


def get_file_size(filename):
    filesize = os.path.getsize(filename)
    print("Your file is ", filesize, "kbs.")
    CHUNK_SIZE = math.ceil(math.ceil(filesize) / 5)
    print("Your file is ", CHUNK_SIZE, " chunks.")
'''

while 1:

    UdpClient.Chunk_Anouncer()



