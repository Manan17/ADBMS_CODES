import socket
conn = socket.socket()
conn.connect(('127.0.0.1',8000))
msg = ""

while msg !="abort":
    if msg == "commit":
        data = conn.recv(1024).decode()
        query = input(data)
        conn.send(query.encode())
    data = conn.recv(1024).decode()
    print(data)
    msg = input("Enter ready, commit or abort: ")
    conn.send(msg.encode())

conn.close()
