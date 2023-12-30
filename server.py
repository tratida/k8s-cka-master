import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", client_address)
        self.csocket.send(bytes("Hi, this is from server!\n", 'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'HGSDC:MSISDN=84981112223,SUD=OBO-1;':
                print('Received command: ', msg)
                self.csocket.send(bytes('EXECUTED\n', 'utf-8'))
            if msg == 'bye':
                break
        print("Client disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 8010
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    client_sock, client_address = server.accept()
    new_thread = ClientThread(client_address, client_sock)
    new_thread.start()