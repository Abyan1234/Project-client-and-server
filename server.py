import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip='127.0.0.1'
port=5500
server.bind((ip,port))
server.listen()
print("server has started")

client=[]
names=[]

def removeName(name):
    if name in names:
        names.remove(name)

def remove(c):
    if c in client:
        client.remove(c)

def broadcast(msg_send,con):
    for c in client:
        if c!=con:
            try:
                c.send(msg_send.encode('utf-8'))
            except:
                remove(c)

def clientThread(con,name):
    con.send("welcome".encode('utf-8'))
    while True:
        try:
            message=con.recv(2048).decode('utf-8')
            if message:
                print(message)
                msg_send=name+message
                broadcast(msg_send,con)
            else:
                remove(con)
                removeName(name)
        except:
            continue

while True:
    con,addr=server.accept()
    con.send('name'.encode('utf-8'))
    name=con.recv(2048).decode('utf-8')
    names.append(name)
    client.append(con)
    message=name+" has joined"
    print(message)
    broadcast(message,con)
    thread1=Thread(target=clientThread,args=(con,name))
    thread1.start()
