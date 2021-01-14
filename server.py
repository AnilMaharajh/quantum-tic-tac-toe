import socket
from _thread import *
import sys


# Uses ideas from https://www.techwithtim.net/tutorials/python-online-game-tutorial/server/


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    while True:
        try:
            # Receives data from client
            data = conn.recv(2048)
            # Encode the data
            reply = data.decode("utf-8")
            # If the client disconnects
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            connection.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()


# Gets your local ipv4
server = socket.gethostbyname(socket.gethostname())
print(server)
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Opens up the port for 2 players
s.listen(2)
print("Waiting for a connection")

# Looks for connections
while True:
    # Accepts connection
    connection, address = s.accept()
    print("Connected to: ", address)

    start_new_thread(threaded_client, (connection,))
