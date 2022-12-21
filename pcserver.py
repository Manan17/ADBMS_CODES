import socket
import sqlite3

host = "127.0.0.1"
port = 8000

conn = socket.socket()
conn.bind((host,port))
conn.listen(2)
c,add = conn.accept()
msg = ""
server_msg = "Prepare"
c.send(server_msg.encode())
while msg!="abort":
    msg = c.recv(1024).decode()
    if msg == "ready":
        #dataconn = sqlite3.connect('test.db')
        message = "Prepared to commit. "
        c.send(message.encode())

    elif msg == "commit":
        message = "Enter query: "
        c.send(message.encode())
        query = c.recv(1024).decode()
        print(query," executed")
        message = "executed!"
        c.send(message.encode())

c.close()