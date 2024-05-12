from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort=6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('the web server is up on port:',serverPort)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode()
        print (message,'::',message.split()[0],':',message.split()[1])
        filename = message.split()[1]
        print (filename,'||',filename[1:])
        f = open(filename[1:])
        outputdata = f.read() 
        f.close() 
        print ("File contents:\n", outputdata)  
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode()) 
        connectionSocket.send(outputdata.encode()) 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        print("IOError:", e)  
        error_message = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(error_message.encode())  
        connectionSocket.close()
        serverSocket.close()
        sys.exit()
 
