import socket

# when use socket, we need create and connect
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET means we use IPv4, AF_INET6 means IPv6. 
# connect
s.connect(('127.0.0.1', 65534)) # IP addr and port. For port, <1024 is for Internet services, so we choose 1024 < any one < 65535. 

# receive welcome form server
d = s.recv(1024) # each time recive 1k bytes.
print('Client receives:%s ' % d.decode('utf-8'))
   
while True:   
    # send data
    usr_in = input('What do you want to send to server?:')
    if usr_in != "stop":
        d = bytes(usr_in, encoding = 'utf-8')
        s.sendall(d) 
        print('Client sends:%s ' % d.decode('utf-8'))

        # receive reply
        d = s.recv(1024) # each time recive 1k bytes.  
        print('Client receives:%s ' % d.decode('utf-8'))
    else:
        break
        
# close socket
s.close()