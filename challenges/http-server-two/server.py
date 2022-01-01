from classes.request import Request
from classes.router import Router
import controller
import socket

HOST, PORT = 'localhost', 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f'Serving HTTP on http://{HOST}:{PORT}')

while True:
    client_connection, _client_address = server.accept()
    request = Request(client_connection.recv(4096).decode())
    response = Router.process(request)
    client_connection.send(response.encode())
    client_connection.close()
