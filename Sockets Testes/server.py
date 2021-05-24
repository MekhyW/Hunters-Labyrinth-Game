import socket
from _thread import *
import sys

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = socket.gethostbyname(socket.gethostname())
print(server_ip)
server = server_ip
port = 5555

try:
    soquete.bind((server, port))

except socket.error as e:
    print(str(e))

soquete.listen(2)
print("Aguardando uma conexão")

currentId = "0"
pos = ["0:50,50", "1:100,100"]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(10000)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = pos[nid][:]
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = soquete.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,))