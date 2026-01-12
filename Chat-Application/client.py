import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
        except:
            print("Connection closed.")
            client.close()
            break

def start_client():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    name = input("Enter your name: ")
    client.send(name.encode())

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input()
        client.send(message.encode())

start_client()
