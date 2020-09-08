from i2p import socket
#sock = socket.socket()
i2plo = socket.socket()
portlol = int(input('Введите порт для локального сервера:'))
#sock.bind(('', portlol))
print('step 2')
#sock.listen()
print('step 3')
#conn, addr = sock.accept()
print('step 4')
i2plo.connect(("q5vc65lf345bakn6z55csafm2oo7hgnuxqzxoyjoj5hhasmjf2ga.b32.i2p", 2389))
print('step 5')
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
    #i2plo.send(b"/login "+bytes(login, 'utf-8')+bytes(password, 'utf-8')+bytes(secretkey, 'utf-8'))
    #if (i2plo.recv(1024) == 'ok'):
    #    break
    #else:
    #    print('Неверный логин, пароль или секретный ключ.')
    break
while True:
    i2plo.send(b'hello!')
    getterl = i2plo.recv(1024)
    print(getterl)
