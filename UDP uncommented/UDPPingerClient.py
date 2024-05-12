from datetime import datetime
from socket import *
from time import time


serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = "Ping"

counter = 10
i = 0

print("Now attempting ", counter, " pings....\n")

while i < counter:
    i+= 1
    print ("\nThis is Ping Attempt Number: ", i)
    print ("There are ", counter - i, "attempts left.")

    a = datetime.now()
    clientSocket.sendto(message.encode(),(serverName,serverPort))

    clientSocket.settimeout(1)

    try:
        modifiedMessage,serverAddress = clientSocket.recvfrom(1024)

        b = datetime.now()
        c = a-b
        print (modifiedMessage.decode())
        print ("elapsed time in microseconds is-> ",c.microseconds)
    except timeout:
        print ("Sorry! Your connection has timed out! Please try again. ")

if i == 10:
    print ("Bye!")

clientSocket.close()

print ("Socket has been closed! No more pings!")


