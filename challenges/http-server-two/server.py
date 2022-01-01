import socket
from classes.request import Request
from classes.response import Response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# so you don't have to change ports when restarting
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 9292))
print('Waiting For Connection...')
server.listen()

while True:
    client_connection, _client_address = server.accept()
    data = client_connection.recv(1024).decode()  # requests from client
    request = Request(data)  # pass decoded to create new Request object

    if request.attributes['Method'] == 'GET':

        # /
        if request.attributes['Resource'] == '/':
            variables = {'phrase': 'Hello World'}
            response = Response('index', variables)

        # /time
        elif request.attributes['Resource'] == '/time':
            variables = {'time': request.attributes['Date']}
            response = Response('time', variables)

        client_connection.send(response.encode())

    client_connection.close()
