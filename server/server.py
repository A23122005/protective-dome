import os
from i2p import socket
def get_i2p_server_address():
    source = os.popen('curl -fsSL 127.0.0.1:7070/?page=i2p_tunnels').read()
    return str(source.split('&#8656;')).split('<br>')[-3].split(' ')[5]
i2p_addres = get_i2p_server_address()
print('Your i2p server adress: ',i2p_addres)
#основной сокет                                                                                                                        
print('step 1')
sock = socket.socket()
print('step 2')
sock.bind(('', 2389))
print('step 3')
sock.listen(5)
print('step 4')
conn, addr = sock.accept()
print('step 5')
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
conn.close()
