#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort=6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('the web server is up on port:',serverPort)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept() 
    #Fill in end
    try:
        #Fill in start
        message = connectionSocket.recv(1024).decode()
        #Fill in end
        print (message,'::',message.split()[0],':',message.split()[1])
        filename = message.split()[1]
        print (filename,'||',filename[1:])
        f = open(filename[1:])
        #Fill in start
        outputdata = f.read() 
        #Fill in end
        f.close()  # Close the file after reading
        print ("File contents:\n", outputdata)  # Debugging print statement
        #Send one HTTP header line into socket
        #Fill in start
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())  # encode string to bytes
        connectionSocket.send(outputdata.encode())  # encode string to bytes
        #Fill in end
        #Send the content of the requested file to the client 
        #this will print raw html
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        #     connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        #Send response message for file not found
        #Fill in start
        print("IOError:", e)  # Debugging print statement
        error_message = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(error_message.encode())  # encode string to bytes
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
        serverSocket.close()
        #Terminate the program after sending the corresponding data
        sys.exit()
 


#ipconfig getifaddr en0 
#to get ip address
#172.30.139.165
#http://172.30.37.206:6789/HelloWorld.html
#http://172.30.37.206:6789/HelloWorld2.html
