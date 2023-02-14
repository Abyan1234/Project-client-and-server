import socket
from threading import Thread

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input("Enter Your Name: ")
ip='127.0.0.1'
port=5500
client.connect((ip,port))
print("Connected with server")


def receive():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='name':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error Occured")
            client.close()
            break

def write():
    while True:
        message=name+":"+input('')
        client.send(message.encode('utf-8'))





thread1=Thread(target=receive)
thread1.start()

thread2=Thread(target=write)
thread2.start()