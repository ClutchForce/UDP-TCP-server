#import socket module
from datetime import datetime
from socket import *
from time import time

#Create a UDP socket
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
#set message to be sent
message = "Ping"

counter = 10
i = 0

print("Now attempting ", counter, " pings....\n")

#while loop to send 10 pings
while i < counter:
    i+= 1
    print ("\nThis is Ping Attempt Number: ", i)
    print ("There are ", counter - i, "attempts left.")

    #start timer
    a = datetime.now()
    clientSocket.sendto(message.encode(),(serverName,serverPort))

    #set timeout to 1 second
    clientSocket.settimeout(1)

    #try to receive message from server
    try:
        #receive message from server
        modifiedMessage,serverAddress = clientSocket.recvfrom(1024)

        #stop timer
        b = datetime.now()
        c = a-b
        #print message and elapsed time
        print (modifiedMessage.decode())
        print ("elapsed time in microseconds is-> ",c.microseconds)
    #if timeout, print error message
    except timeout:
        print ("Sorry! Your connection has timed out! Please try again. ")

if i == 10:
    print ("Bye!")

#close socket
clientSocket.close()

print ("Socket has been closed! No more pings!")


