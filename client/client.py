#from random import randint
from i2p import socket
import os

sock = socket.socket()
i2plo = socket.socket()
portlol = int(input('Введите порт для локального сервера:'))
sock.bind(('', portlol))
sock.listen()
conn, addr = sock.accept()
i2plo.connect(("i2p-projekt.i2p", 80))
while(True):
    while(True):
        login =  str(input('Введите логин:'))
        if (' ' in login):
            print('Не испуользуйте пробел.')
        else:
            break
    while(True):
        password = str(input('Введите пароль:'))
        if (' ' in password):
            print('Не испуользуйте пробел.')
        else:
            break
    while(True):
        secretkey = str(input('Введите секретный ключ:'))
        if (' ' in secretkey):
            print('Не испуользуйте пробел.')
        else:
            break
    #test auth
    i2plo.send(b"/login "+bytes(login, 'utf-8')+bytes(password, 'utf-8')+bytes(secretkey, 'utf-8'))
    if (i2plo.recv(1024) == 'ok'):
        break
    else:
        print('Неверный логин, пароль или секретный ключ.')

while True:
    getterl = sock.recv(1024)
    i2plo.send('/data '+getterl)
