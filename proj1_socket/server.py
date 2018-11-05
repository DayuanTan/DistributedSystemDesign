import socket
import threading

# create
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
s.bind(('127.0.0.1',65534))
# listen
s.listen(10) # 10 means I can listen maximum 10 connections.
print('Server is waiting for connection...')

# process communication with clients
def tcplink(sock, addr):
    print('Accept new connection form %s:%s...' % addr)
    wel = 'Welcome client' + (str(addr))
    sock.send(bytes(wel, encoding = 'utf-8'))
    while True:
        data = sock.recv(1024)
        if not data:
            break
        data = data.decode('utf-8')
        print('received from ' + str(addr) + ':' + data)
        r_data = data[::-1].encode('utf-8') # [::-1] is used to reverse strings.
        sock.sendall(r_data)
        print('reply to ' + str(addr) + ':' + r_data.decode('utf-8'))
    sock.close()
    print('Connection form %s:%s closed.' % addr)

# A forever loop to accept message form clients.
while True:
    # accept a new connection
    sock, addr = s.accept()
    # create a thread for each client
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

