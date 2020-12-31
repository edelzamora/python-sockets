import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"
SERVER = "192.168.0.14"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_connection():
    client.connect(ADDR)
    active_connection = True
    while active_connection:
        usr_msg = input("Type msg: ")
        if usr_msg == DISCONNECT_MESSAGE:
            active_connection = False
        send(usr_msg)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

start_connection()