import socket

# when use socket, we need create and connect
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET means we use IPv4, AF_INET6 means IPv6. 
# connect
s.connect(('127.0.0.1', 65534)) # IP addr and port. For port, <1024 is for Internet services, so we choose 1024 < any one < 65535. 

# receive welcome form server
d = s.recv(1024) # each time recive 1k bytes.
print('Client receives:%s ' % d.decode('utf-8'))
   
# send data
d = b'ADVANCE'
s.sendall(d) # From python doc: Unlike send(), sendall() continues to send data from string until either all data has been sent or an error occurs.
print('Client sends:%s ' % d.decode('utf-8'))

# receive reply
d = s.recv(1024) # each time recive 1k bytes.  
print('Client receives:%s ' % d.decode('utf-8'))

# close socket
s.close()
